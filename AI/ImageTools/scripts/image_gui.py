from __future__ import annotations

import json
import threading
import time
import uuid
import webbrowser
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import unquote

from image_organizer import (
    DEFAULT_AI_LABELS,
    DEFAULT_AI_MODEL,
    DEFAULT_CHARACTER,
    DEFAULT_CORRECTIONS,
    DEFAULT_LOG_DIR,
    DEFAULT_OUTPUT_ROOT,
    DEFAULT_SOURCE_DIR,
    analyze_with_pillow,
    image_meta,
    iter_images,
    organize_images,
)
from rating_rules import RATING_CATEGORIES


HOST = "127.0.0.1"
PORT = 8766


@dataclass
class OrganizeJob:
    id: str
    source_dir: Path
    output_root: Path
    character: str
    recursive: bool
    dry_run: bool
    log_dir: Path
    rename: bool
    use_ai: bool
    ai_model: Path
    ai_labels: Path
    corrections_path: Path
    ai_flip_binary_labels: bool
    ai_debug_outputs: bool
    force_review_on_suspicious_sfw: bool
    confidence_threshold: float
    review_uncertain: bool
    status: str = "queued"
    current: str = ""
    progress: float = 0
    logs: list[str] = field(default_factory=list)
    done: bool = False


JOBS: dict[str, OrganizeJob] = {}
JOBS_LOCK = threading.Lock()


HTML = r"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Aetherion Image Organizer</title>
  <style>
    :root {
      color-scheme: dark;
      --bg: #10141a;
      --panel: #17212b;
      --panel-2: #222d38;
      --line: #354656;
      --text: #f2f7fb;
      --muted: #aab8c5;
      --green: #4fe0a3;
      --gold: #f0bf5a;
      --rose: #ff7d94;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      background:
        linear-gradient(135deg, rgba(79, 224, 163, .13), transparent 34%),
        linear-gradient(315deg, rgba(240, 191, 90, .12), transparent 38%),
        var(--bg);
      color: var(--text);
      font: 15px/1.45 "Segoe UI", system-ui, sans-serif;
    }
    button, input, select { font: inherit; }
    .shell { width: min(1180px, calc(100vw - 32px)); margin: 0 auto; padding: 26px 0; }
    header {
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 22px;
      align-items: center;
      margin-bottom: 22px;
    }
    h1 { margin: 0; font-size: 34px; line-height: 1.05; letter-spacing: 0; }
    h2 { margin: 0; font-size: 18px; }
    .subtitle { margin: 8px 0 0; color: var(--muted); max-width: 680px; }
    .mosaic {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      grid-auto-rows: 34px;
      gap: 7px;
      padding: 12px;
      background: rgba(23, 33, 43, .9);
      border: 1px solid rgba(255,255,255,.08);
    }
    .tile { background: #263544; border: 1px solid rgba(255,255,255,.08); }
    .tile:nth-child(2n) { background: #1f4b46; }
    .tile:nth-child(3n) { background: #5b4931; }
    .tile:nth-child(5n) { background: #45334c; }
    .tile.wide { grid-column: span 2; }
    .tile.tall { grid-row: span 2; }
    .grid {
      display: grid;
      grid-template-columns: minmax(0, 1.4fr) minmax(330px, .9fr);
      gap: 18px;
    }
    .panel {
      background: rgba(23, 33, 43, .94);
      border: 1px solid rgba(255,255,255,.08);
      padding: 18px;
    }
    .top { display: flex; align-items: center; justify-content: space-between; gap: 16px; margin-bottom: 14px; }
    .muted { color: var(--muted); }
    label { display: block; color: var(--muted); margin: 14px 0 6px; }
    input[type="text"], select {
      width: 100%;
      color: var(--text);
      background: #111922;
      border: 1px solid var(--line);
      padding: 10px;
      outline: none;
    }
    .row { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
    .checkline { display: flex; gap: 10px; align-items: center; color: var(--text); margin-top: 12px; }
    .checkline input { width: 18px; height: 18px; }
    .actions { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; }
    button {
      border: 0;
      background: #2a3a4a;
      color: var(--text);
      padding: 10px 13px;
      cursor: pointer;
      min-height: 40px;
    }
    button:hover { background: #395067; }
    button.primary { width: 100%; background: var(--green); color: #04130d; font-weight: 700; margin-top: 14px; }
    button.primary:hover { background: #72edba; }
    button:disabled { opacity: .55; cursor: not-allowed; }
    .filebox { min-height: 430px; max-height: 520px; overflow: auto; background: #111922; border: 1px solid rgba(255,255,255,.08); }
    table { width: 100%; border-collapse: collapse; }
    th, td { border-bottom: 1px solid rgba(255,255,255,.08); padding: 10px 8px; text-align: left; vertical-align: middle; }
    th { color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: .04em; background: #222d38; }
    td.size { text-align: right; white-space: nowrap; color: #d9f8e9; }
    .meter { height: 14px; background: #2a3a4a; border: 1px solid rgba(255,255,255,.08); overflow: hidden; margin-top: 12px; }
    .fill { height: 100%; width: 0%; background: linear-gradient(90deg, var(--green), var(--gold)); transition: width .25s ease; }
    .status {
      margin-top: 12px;
      padding: 12px;
      background: #111922;
      border: 1px solid rgba(255,255,255,.08);
      min-height: 46px;
    }
    .log {
      height: 220px;
      overflow: auto;
      margin-top: 12px;
      padding: 12px;
      background: #0b1117;
      border: 1px solid rgba(255,255,255,.08);
      color: #ddf7e9;
      font: 13px/1.5 Consolas, monospace;
      white-space: pre-wrap;
    }
    .danger { color: var(--rose); }
    @media (max-width: 900px) {
      header, .grid, .row { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <main class="shell">
    <header>
      <div>
        <h1>Aetherion Image Organizer</h1>
        <p class="subtitle">Rate and copy character images with local Pillow analysis, optional CPU-only AI hooks, copy-only safety, dry-run previews, and JSON logs.</p>
      </div>
      <div class="mosaic" aria-hidden="true">
        <div class="tile tall"></div><div class="tile wide"></div><div class="tile"></div><div class="tile tall"></div>
        <div class="tile"></div><div class="tile"></div><div class="tile wide"></div><div class="tile"></div>
        <div class="tile wide"></div><div class="tile"></div><div class="tile tall"></div><div class="tile"></div>
        <div class="tile"></div><div class="tile wide"></div><div class="tile"></div><div class="tile"></div>
      </div>
    </header>

    <section class="grid">
      <div class="panel">
        <div class="top">
          <div>
            <h2>Detected Images</h2>
            <div class="muted">Scan supported PNG, JPG, JPEG, and WEBP files before organizing.</div>
          </div>
          <strong id="count">0 found</strong>
        </div>
        <label for="sourceDir">Source folder</label>
        <input id="sourceDir" type="text">
        <div class="actions">
          <button id="scan">Scan Source</button>
        </div>
        <div class="filebox">
          <table>
            <thead><tr><th>File</th><th>Pixels</th><th>Skin</th><th>Neon</th><th>Size</th></tr></thead>
            <tbody id="files"></tbody>
          </table>
        </div>
      </div>

      <aside class="panel">
        <h2>Rating Organizer</h2>
        <label for="targetRoot">Output image root</label>
        <input id="targetRoot" type="text">
        <label for="character">Default character folder</label>
        <input id="character" type="text">
        <label for="reportDir">JSON log folder</label>
        <input id="reportDir" type="text">
        <label for="aiModel">Local ONNX model</label>
        <input id="aiModel" type="text">
        <label for="aiLabels">Rating labels</label>
        <input id="aiLabels" type="text">
        <label for="correctionsPath">Manual corrections</label>
        <input id="correctionsPath" type="text">
        <div class="row">
          <div>
            <label for="confidence">Review threshold</label>
            <input id="confidence" type="number" min="0.1" max="0.99" step="0.01" value="0.70">
          </div>
          <div>
            <label>Mode</label>
            <div class="muted" style="padding:10px 0">Copy-only</div>
          </div>
        </div>
        <div class="muted" style="margin-top:12px">Rating folders: <span id="categories"></span></div>
        <label class="checkline"><input id="recursive" type="checkbox" checked> Scan recursively</label>
        <label class="checkline"><input id="dryRun" type="checkbox"> Dry run only</label>
        <label class="checkline"><input id="reviewUncertain" type="checkbox" checked> Send low-confidence ratings to Review_Needed</label>
        <label class="checkline"><input id="useAi" type="checkbox"> Try optional local AI if installed</label>
        <label class="checkline"><input id="forceSuspiciousSfw" type="checkbox" checked> Review suspicious AI SFW results</label>
        <label class="checkline"><input id="aiDebugOutputs" type="checkbox" checked> Log AI debug outputs</label>
        <label class="checkline"><input id="aiFlipBinaryLabels" type="checkbox"> Flip binary SFW/NSFW labels</label>
        <label class="checkline"><input id="rename" type="checkbox" checked> Generate clean target filenames</label>
        <button id="organize" class="primary">Organize Images</button>

        <div class="meter"><div id="fill" class="fill"></div></div>
        <div id="status" class="status">Ready</div>
        <div id="log" class="log"></div>
      </aside>
    </section>
  </main>

  <script>
    const $ = (id) => document.getElementById(id);
    let currentJob = null;

    function sizeMb(bytes) {
      return `${(bytes / 1024 / 1024).toFixed(2)} MB`;
    }

    async function api(path, options = {}) {
      const response = await fetch(path, {
        headers: { "content-type": "application/json" },
        ...options,
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || response.statusText);
      return data;
    }

    function renderFiles(files) {
      const body = $("files");
      body.innerHTML = "";
      for (const file of files) {
        const row = document.createElement("tr");
        row.innerHTML = `<td>${file.name}<div class="muted">${file.modified}</div></td><td>${file.pixels}</td><td>${file.skin}</td><td>${file.neon}</td><td class="size">${sizeMb(file.size)}</td>`;
        body.appendChild(row);
      }
      $("count").textContent = `${files.length} found`;
    }

    async function loadDefaults() {
      const data = await api("/api/defaults");
      $("sourceDir").value = data.source_dir;
      $("targetRoot").value = data.output_root;
      $("character").value = data.default_character;
      $("reportDir").value = data.report_dir;
      $("aiModel").value = data.ai_model;
      $("aiLabels").value = data.ai_labels;
      $("correctionsPath").value = data.corrections;
      $("categories").textContent = data.categories.join(", ");
      await scan();
    }

    async function scan() {
      $("status").textContent = "Scanning source folder";
      const data = await api("/api/scan", {
        method: "POST",
        body: JSON.stringify({ source_dir: $("sourceDir").value, recursive: $("recursive").checked }),
      });
      renderFiles(data.files);
      $("status").textContent = `Found ${data.files.length} image(s).`;
    }

    async function organize() {
      $("organize").disabled = true;
      $("fill").style.width = "0%";
      $("log").textContent = "";
      const data = await api("/api/jobs", {
        method: "POST",
        body: JSON.stringify({
          source_dir: $("sourceDir").value,
          output_root: $("targetRoot").value,
          character: $("character").value,
          recursive: $("recursive").checked,
          dry_run: $("dryRun").checked,
          log_dir: $("reportDir").value,
          rename: $("rename").checked,
          use_ai: $("useAi").checked,
          ai_model: $("aiModel").value,
          ai_labels: $("aiLabels").value,
          corrections: $("correctionsPath").value,
          ai_flip_binary_labels: $("aiFlipBinaryLabels").checked,
          ai_debug_outputs: $("aiDebugOutputs").checked,
          force_review_on_suspicious_sfw: $("forceSuspiciousSfw").checked,
          confidence_threshold: Number($("confidence").value),
          review_uncertain: $("reviewUncertain").checked,
        }),
      });
      currentJob = data.id;
      pollJob();
    }

    async function pollJob() {
      if (!currentJob) return;
      const data = await api(`/api/jobs/${currentJob}`);
      $("fill").style.width = `${data.progress}%`;
      $("status").textContent = data.current || data.status;
      $("log").textContent = data.logs.join("\n") + (data.logs.length ? "\n" : "");
      if (!data.done) {
        setTimeout(pollJob, 700);
      } else {
        $("organize").disabled = false;
        currentJob = null;
        scan().catch(() => {});
      }
    }

    $("scan").addEventListener("click", () => scan().catch(error => {
      $("status").innerHTML = `<span class="danger">${error.message}</span>`;
    }));
    $("organize").addEventListener("click", () => organize().catch(error => {
      $("organize").disabled = false;
      $("status").innerHTML = `<span class="danger">${error.message}</span>`;
    }));
    loadDefaults().catch(error => {
      $("status").innerHTML = `<span class="danger">${error.message}</span>`;
    });
  </script>
</body>
</html>
"""


class ImageGuiHandler(BaseHTTPRequestHandler):
    server_version = "AetherionImageOrganizer/1.0"

    def do_GET(self) -> None:
        if self.path == "/":
            self._send_html(HTML)
            return

        if self.path == "/api/defaults":
            self._send_json(
                {
                    "source_dir": str(DEFAULT_SOURCE_DIR.resolve()),
                    "output_root": str(DEFAULT_OUTPUT_ROOT.resolve()),
                    "report_dir": str(DEFAULT_LOG_DIR.resolve()),
                    "ai_model": str(DEFAULT_AI_MODEL.resolve()),
                    "ai_labels": str(DEFAULT_AI_LABELS.resolve()),
                    "corrections": str(DEFAULT_CORRECTIONS.resolve()),
                    "categories": list(RATING_CATEGORIES),
                    "default_character": DEFAULT_CHARACTER,
                }
            )
            return

        if self.path.startswith("/api/jobs/"):
            job_id = unquote(self.path.rsplit("/", 1)[-1])
            with JOBS_LOCK:
                job = JOBS.get(job_id)
                if not job:
                    self._send_json({"error": "Job not found"}, status=404)
                    return
                self._send_json(job_payload(job))
            return

        self._send_json({"error": "Not found"}, status=404)

    def do_POST(self) -> None:
        if self.path == "/api/scan":
            payload = self._read_json()
            try:
                source_dir = Path(payload.get("source_dir", DEFAULT_SOURCE_DIR))
                recursive = bool(payload.get("recursive", False))
                files = image_payloads(source_dir, recursive=recursive)
            except BaseException as error:
                self._send_json({"error": str(error)}, status=400)
                return
            self._send_json({"files": files})
            return

        if self.path == "/api/jobs":
            payload = self._read_json()
            try:
                job = OrganizeJob(
                    id=uuid.uuid4().hex,
                    source_dir=Path(payload.get("source_dir", DEFAULT_SOURCE_DIR)),
                    output_root=Path(payload.get("output_root", DEFAULT_OUTPUT_ROOT)),
                    character=str(payload.get("character", DEFAULT_CHARACTER)),
                    recursive=bool(payload.get("recursive", False)),
                    dry_run=bool(payload.get("dry_run", False)),
                    log_dir=Path(payload.get("log_dir", DEFAULT_LOG_DIR)),
                    rename=bool(payload.get("rename", True)),
                    use_ai=bool(payload.get("use_ai", False)),
                    ai_model=Path(payload.get("ai_model", DEFAULT_AI_MODEL)),
                    ai_labels=Path(payload.get("ai_labels", DEFAULT_AI_LABELS)),
                    corrections_path=Path(payload.get("corrections", DEFAULT_CORRECTIONS)),
                    ai_flip_binary_labels=bool(payload.get("ai_flip_binary_labels", False)),
                    ai_debug_outputs=bool(payload.get("ai_debug_outputs", True)),
                    force_review_on_suspicious_sfw=bool(payload.get("force_review_on_suspicious_sfw", True)),
                    confidence_threshold=float(payload.get("confidence_threshold", 0.70)),
                    review_uncertain=bool(payload.get("review_uncertain", True)),
                )
            except BaseException as error:
                self._send_json({"error": f"Invalid job request: {error}"}, status=400)
                return

            with JOBS_LOCK:
                JOBS[job.id] = job
            threading.Thread(target=run_job, args=(job,), daemon=True).start()
            self._send_json({"id": job.id})
            return

        self._send_json({"error": "Not found"}, status=404)

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


def image_payloads(source_dir: Path, recursive: bool) -> list[dict[str, Any]]:
    payloads: list[dict[str, Any]] = []
    for path in iter_images(source_dir, recursive=recursive):
        signals = analyze_with_pillow(path)
        asset = image_meta(path, signals)
        pixels = f"{asset.width}x{asset.height}" if asset.width and asset.height else "unknown"
        skin = f"{signals.skin_like_ratio:.3f}" if signals.skin_like_ratio is not None else "n/a"
        neon = f"{signals.neon_ratio:.3f}" if signals.neon_ratio is not None else "n/a"
        payloads.append(
            {
                "path": str(asset.path),
                "name": asset.path.name,
                "folder": str(asset.path.parent),
                "size": asset.size_bytes,
                "modified": asset.modified_at,
                "pixels": pixels,
                "skin": skin,
                "neon": neon,
            }
        )
    return payloads


def job_payload(job: OrganizeJob) -> dict[str, Any]:
    return {
        "id": job.id,
        "status": job.status,
        "current": job.current,
        "progress": round(job.progress, 1),
        "logs": job.logs,
        "done": job.done,
    }


def update_job(job: OrganizeJob, **changes: Any) -> None:
    with JOBS_LOCK:
        for key, value in changes.items():
            setattr(job, key, value)


def append_log(job: OrganizeJob, message: str) -> None:
    with JOBS_LOCK:
        job.logs.append(message)


def run_job(job: OrganizeJob) -> None:
    update_job(job, status="running", current="Organizing images")
    try:
        results = organize_images(
            source_dir=job.source_dir,
            output_root=job.output_root,
            character=job.character,
            recursive=job.recursive,
            dry_run=job.dry_run,
            log_dir=job.log_dir,
            rename=job.rename,
            use_ai=job.use_ai,
            ai_model=job.ai_model,
            ai_labels=job.ai_labels,
            corrections_path=job.corrections_path,
            ai_flip_binary_labels=job.ai_flip_binary_labels,
            ai_debug_outputs=job.ai_debug_outputs,
            force_review_on_suspicious_sfw=job.force_review_on_suspicious_sfw,
            confidence_threshold=job.confidence_threshold,
            review_uncertain=job.review_uncertain,
        )
    except BaseException as error:
        update_job(job, status="failed", current=str(error), done=True)
        append_log(job, f"FAILED: {error}")
        return

    results, report_paths = results
    total = len(results)
    for index, result in enumerate(results, start=1):
        prefix = "Would copy" if result.dry_run else "Copied"
        ai = "ai" if result.used_ai else "rules"
        append_log(
            job,
            f"{prefix}: {Path(result.source).name} -> {result.category} "
            f"({result.confidence:.2f}, {ai}) | {result.reason} | {result.target}",
        )
        update_job(job, progress=index / total * 100 if total else 100)

    if total == 0:
        update_job(job, progress=100)
        append_log(job, "No images found.")

    for label, path in report_paths.items():
        append_log(job, f"{label}: {path}")

    update_job(job, status="complete", current=f"Finished {total} image(s).", done=True)


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), ImageGuiHandler)
    url = f"http://{HOST}:{PORT}/"
    print(f"Aetherion Image Organizer running at {url}")
    print("Press Ctrl+C to stop.")

    threading.Thread(target=open_browser, args=(url,), daemon=True).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping Aetherion Image Organizer.")
    finally:
        server.server_close()


def open_browser(url: str) -> None:
    time.sleep(0.5)
    webbrowser.open(url)


if __name__ == "__main__":
    main()
