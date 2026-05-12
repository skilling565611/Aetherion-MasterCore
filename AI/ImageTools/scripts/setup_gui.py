from __future__ import annotations

import importlib.util
import argparse
import json
import subprocess
import sys
import threading
import time
import uuid
import webbrowser
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any


HOST = "127.0.0.1"
PORT = 8767

REPO_ROOT = Path(__file__).resolve().parents[3]
PROJECT_DIR = REPO_ROOT / "AI/ImageTools"
REQUIREMENTS_DIR = PROJECT_DIR / "Requirements"
CONFIGS_DIR = PROJECT_DIR / "Configs"
LOGS_DIR = PROJECT_DIR / "Logs"
MODELS_DIR = PROJECT_DIR / "models"

DEPENDENCIES = (
    ("Pillow", "PIL", "image"),
    ("ImageHash", "imagehash", "image"),
    ("numpy", "numpy", "ai"),
    ("onnxruntime", "onnxruntime", "ai"),
)

INSTALL_COMMANDS = {
    "base": [sys.executable, "-m", "pip", "install", "-r", "AI/ImageTools/Requirements/base.txt"],
    "image": [sys.executable, "-m", "pip", "install", "-r", "AI/ImageTools/Requirements/image.txt"],
    "ai": [sys.executable, "-m", "pip", "install", "-r", "AI/ImageTools/Requirements/ai-optional.txt"],
    "dev": [sys.executable, "-m", "pip", "install", "-r", "AI/ImageTools/Requirements/dev.txt"],
    "project": [sys.executable, "-m", "pip", "install", "-e", "AI/ImageTools"],
}


@dataclass
class SetupJob:
    id: str
    label: str
    command: list[str]
    status: str = "queued"
    progress: int = 0
    logs: list[str] = field(default_factory=list)
    done: bool = False
    return_code: int | None = None


JOBS: dict[str, SetupJob] = {}
JOBS_LOCK = threading.Lock()


HTML = r"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Aetherion ImageTools Setup</title>
  <style>
    :root {
      color-scheme: dark;
      --bg: #10151b;
      --panel: #18232d;
      --panel2: #22303c;
      --line: #344755;
      --text: #f3f8fb;
      --muted: #aebbc7;
      --green: #52daa4;
      --gold: #efc45d;
      --red: #ff8190;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      background:
        linear-gradient(120deg, rgba(82, 218, 164, .14), transparent 36%),
        linear-gradient(300deg, rgba(239, 196, 93, .1), transparent 42%),
        var(--bg);
      color: var(--text);
      font: 15px/1.45 "Segoe UI", system-ui, sans-serif;
    }
    button, input { font: inherit; }
    .shell { width: min(1120px, calc(100vw - 32px)); margin: 0 auto; padding: 28px 0; }
    h1 { margin: 0; font-size: 32px; letter-spacing: 0; }
    h2 { margin: 0 0 12px; font-size: 18px; }
    .sub { color: var(--muted); margin: 8px 0 0; max-width: 780px; }
    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 22px; }
    .panel {
      background: rgba(24, 35, 45, .96);
      border: 1px solid rgba(255,255,255,.08);
      padding: 18px;
    }
    .wide { grid-column: 1 / -1; }
    .kv { display: grid; grid-template-columns: 160px 1fr; gap: 8px 14px; }
    .key { color: var(--muted); }
    .value { overflow-wrap: anywhere; }
    .deps { display: grid; gap: 8px; }
    .dep {
      display: flex;
      justify-content: space-between;
      gap: 12px;
      padding: 10px;
      background: #111920;
      border: 1px solid rgba(255,255,255,.07);
    }
    .ok { color: var(--green); font-weight: 700; }
    .missing { color: var(--red); font-weight: 700; }
    .actions { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }
    button {
      min-height: 42px;
      border: 0;
      background: #2d3e4c;
      color: var(--text);
      cursor: pointer;
      padding: 10px 12px;
      text-align: left;
    }
    button:hover { background: #3b5365; }
    button.primary { background: var(--green); color: #06140f; font-weight: 700; }
    button.warn { background: var(--gold); color: #1e1603; font-weight: 700; }
    button:disabled { opacity: .55; cursor: not-allowed; }
    label.confirm {
      display: flex;
      gap: 10px;
      align-items: center;
      margin: 12px 0;
      color: var(--text);
      background: #111920;
      border: 1px solid rgba(255,255,255,.07);
      padding: 10px;
    }
    label.confirm input { width: 18px; height: 18px; }
    .note { color: var(--muted); margin-top: 10px; }
    .log {
      min-height: 220px;
      max-height: 420px;
      overflow: auto;
      white-space: pre-wrap;
      font: 13px/1.5 Consolas, monospace;
      background: #0b1117;
      border: 1px solid rgba(255,255,255,.08);
      padding: 12px;
      color: #e0f7ea;
    }
    .progress {
      height: 16px;
      background: #111920;
      border: 1px solid rgba(255,255,255,.08);
      overflow: hidden;
      margin: 12px 0;
    }
    .bar {
      width: 0%;
      height: 100%;
      background: linear-gradient(90deg, var(--green), var(--gold));
      transition: width .25s ease;
    }
    .progress-row {
      display: flex;
      justify-content: space-between;
      color: var(--muted);
      gap: 12px;
    }
    @media (max-width: 820px) {
      .grid, .actions, .kv { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <main class="shell">
    <h1>Aetherion ImageTools Setup</h1>
    <p class="sub">Check the local ImageTools Python environment, create required folders, and install optional add-ons only after you explicitly approve them.</p>

    <section class="grid">
      <div class="panel">
        <h2>Environment</h2>
        <div id="env" class="kv"></div>
        <p class="note">Run this GUI with the ImageTools venv Python to keep installs removable later.</p>
      </div>

      <div class="panel">
        <h2>Dependency Status</h2>
        <div id="deps" class="deps"></div>
      </div>

      <div class="panel wide">
        <h2>Install Buttons</h2>
        <label class="confirm">
          <input id="confirm" type="checkbox">
          I approve running pip install commands inside the Python environment shown above.
        </label>
        <div class="actions">
          <button class="primary" data-action="project">Install Project Editable</button>
          <button data-action="base">Install Base</button>
          <button data-action="image">Install Image Tools</button>
          <button class="warn" data-action="ai">Install Optional CPU AI</button>
          <button data-action="dev">Install Dev Tools</button>
          <button id="refresh">Refresh Status</button>
        </div>
        <p class="note">The AI button installs only numpy and onnxruntime. It does not install torch, transformers, tensorflow, or other heavy AI packages.</p>
      </div>

      <div class="panel wide">
        <h2>Install Log</h2>
        <div class="progress-row">
          <span id="progressLabel">Ready</span>
          <span id="progressValue">0%</span>
        </div>
        <div class="progress"><div id="progressBar" class="bar"></div></div>
        <div id="log" class="log">Ready</div>
      </div>
    </section>
  </main>

  <script>
    const $ = (id) => document.getElementById(id);
    let activeJob = null;

    async function api(path, options = {}) {
      const response = await fetch(path, {
        headers: { "content-type": "application/json" },
        ...options,
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || response.statusText);
      return data;
    }

    function renderStatus(data) {
      $("env").innerHTML = `
        <div class="key">Python</div><div class="value">${data.python_version}</div>
        <div class="key">Executable</div><div class="value">${data.executable}</div>
        <div class="key">Project</div><div class="value">${data.project_dir}</div>
        <div class="key">pip</div><div class="value">${data.pip || "missing"}</div>
        <div class="key">Folders</div><div class="value">${data.folders.join("<br>")}</div>
      `;
      $("deps").innerHTML = data.dependencies.map(dep => `
        <div class="dep">
          <span>${dep.name}<br><span class="key">${dep.group}</span></span>
          <span class="${dep.installed ? "ok" : "missing"}">${dep.installed ? "installed" : "missing"}</span>
        </div>
      `).join("");
    }

    async function refresh() {
      const data = await api("/api/status");
      renderStatus(data);
    }

    async function startInstall(action) {
      if (!$("confirm").checked) {
        $("log").textContent = "Install blocked. Check the approval box first.";
        return;
      }
      const data = await api("/api/install", {
        method: "POST",
        body: JSON.stringify({ action, approved: true }),
      });
      activeJob = data.id;
      poll();
    }

    async function poll() {
      if (!activeJob) return;
      const data = await api(`/api/jobs/${activeJob}`);
      $("progressLabel").textContent = data.status;
      $("progressValue").textContent = `${data.progress}%`;
      $("progressBar").style.width = `${data.progress}%`;
      $("log").textContent = data.logs.join("\n") || data.status;
      if (!data.done) {
        setTimeout(poll, 800);
      } else {
        activeJob = null;
        await refresh();
      }
    }

    document.querySelectorAll("[data-action]").forEach(button => {
      button.addEventListener("click", () => startInstall(button.dataset.action).catch(error => {
        $("log").textContent = error.message;
      }));
    });
    $("refresh").addEventListener("click", () => refresh().catch(error => {
      $("log").textContent = error.message;
    }));
    refresh().catch(error => {
      $("log").textContent = error.message;
    });
  </script>
</body>
</html>
"""


class SetupGuiHandler(BaseHTTPRequestHandler):
    server_version = "AetherionImageToolsSetup/1.0"

    def do_GET(self) -> None:
        if self.path == "/":
            self._send_html(HTML)
            return
        if self.path == "/api/status":
            ensure_folders()
            self._send_json(status_payload())
            return
        if self.path.startswith("/api/jobs/"):
            job_id = self.path.rsplit("/", 1)[-1]
            with JOBS_LOCK:
                job = JOBS.get(job_id)
                if job is None:
                    self._send_json({"error": "Job not found"}, status=404)
                    return
                self._send_json(job_payload(job))
            return
        self._send_json({"error": "Not found"}, status=404)

    def do_POST(self) -> None:
        if self.path != "/api/install":
            self._send_json({"error": "Not found"}, status=404)
            return

        payload = self._read_json()
        action = str(payload.get("action", ""))
        approved = bool(payload.get("approved", False))
        if not approved:
            self._send_json({"error": "Install requires user approval"}, status=403)
            return
        if action not in INSTALL_COMMANDS:
            self._send_json({"error": f"Unknown install action: {action}"}, status=400)
            return

        job = SetupJob(id=uuid.uuid4().hex, label=action, command=INSTALL_COMMANDS[action])
        with JOBS_LOCK:
            JOBS[job.id] = job
        threading.Thread(target=run_install_job, args=(job,), daemon=True).start()
        self._send_json({"id": job.id})

    def log_message(self, format: str, *args: Any) -> None:
        return

    def _read_json(self) -> dict[str, Any]:
        length = int(self.headers.get("content-length", "0"))
        if length == 0:
            return {}
        return json.loads(self.rfile.read(length).decode("utf-8"))

    def _send_html(self, value: str) -> None:
        data = value.encode("utf-8")
        self.send_response(200)
        self.send_header("content-type", "text/html; charset=utf-8")
        self.send_header("content-length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_json(self, value: dict[str, Any], status: int = 200) -> None:
        data = json.dumps(value).encode("utf-8")
        self.send_response(status)
        self.send_header("content-type", "application/json; charset=utf-8")
        self.send_header("content-length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def ensure_folders() -> None:
    for folder in (REQUIREMENTS_DIR, CONFIGS_DIR, LOGS_DIR, MODELS_DIR):
        folder.mkdir(parents=True, exist_ok=True)


def pip_version() -> str:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "--version"],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def status_payload() -> dict[str, Any]:
    return {
        "python_version": sys.version.split()[0],
        "executable": sys.executable,
        "project_dir": str(PROJECT_DIR),
        "pip": pip_version(),
        "folders": [str(path) for path in (REQUIREMENTS_DIR, CONFIGS_DIR, LOGS_DIR, MODELS_DIR)],
        "dependencies": [
            {
                "name": display_name,
                "import_name": import_name,
                "group": group,
                "installed": importlib.util.find_spec(import_name) is not None,
            }
            for display_name, import_name, group in DEPENDENCIES
        ],
    }


def job_payload(job: SetupJob) -> dict[str, Any]:
    return {
        "id": job.id,
        "label": job.label,
        "status": job.status,
        "progress": job.progress,
        "logs": job.logs,
        "done": job.done,
        "return_code": job.return_code,
    }


def append_log(job: SetupJob, message: str) -> None:
    with JOBS_LOCK:
        job.logs.append(message)


def update_job(job: SetupJob, **changes: Any) -> None:
    with JOBS_LOCK:
        for key, value in changes.items():
            setattr(job, key, value)


def run_install_job(job: SetupJob) -> None:
    update_job(job, status="starting", progress=5)
    append_log(job, f"Approved install: {job.label}")
    append_log(job, f"Using Python: {sys.executable}")
    append_log(job, f"Command: {' '.join(job.command)}")
    update_job(job, status="running pip install", progress=15)

    process = subprocess.Popen(
        job.command,
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    assert process.stdout is not None
    for line in process.stdout:
        append_log(job, line.rstrip())
        if job.progress < 90:
            update_job(job, progress=min(job.progress + 3, 90))
    update_job(job, status="finishing", progress=95)
    return_code = process.wait()
    update_job(
        job,
        return_code=return_code,
        done=True,
        status="complete" if return_code == 0 else "failed",
        progress=100,
    )
    append_log(job, f"Finished with exit code {return_code}")


def open_browser(url: str) -> None:
    time.sleep(0.5)
    webbrowser.open(url)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Local browser GUI for ImageTools setup.")
    parser.add_argument("--check-status", action="store_true", help="Print environment status as JSON and exit.")
    parser.add_argument("--no-browser", action="store_true", help="Start the server without opening a browser tab.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ensure_folders()
    if args.check_status:
        print(json.dumps(status_payload(), indent=2))
        return

    server = ThreadingHTTPServer((HOST, PORT), SetupGuiHandler)
    url = f"http://{HOST}:{PORT}/"
    print(f"Aetherion ImageTools Setup GUI running at {url}")
    print("Use the approval checkbox before running install buttons.")
    print("Press Ctrl+C to stop.")

    if not args.no_browser:
        threading.Thread(target=open_browser, args=(url,), daemon=True).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping Aetherion ImageTools Setup GUI.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
