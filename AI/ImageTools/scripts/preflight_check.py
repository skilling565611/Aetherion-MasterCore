from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


@dataclass(frozen=True)
class CommandResult:
    returncode: int
    stdout: str
    stderr: str


def run_command(command: list[str], timeout: int = 15) -> CommandResult:
    """Run a read-only command and capture output without raising."""

    try:
        completed = subprocess.run(
            command,
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
    except FileNotFoundError as error:
        return CommandResult(127, "", str(error))
    except subprocess.TimeoutExpired as error:
        return CommandResult(124, error.stdout or "", error.stderr or "command timed out")

    return CommandResult(completed.returncode, completed.stdout.strip(), completed.stderr.strip())


def find_git_dir() -> Path:
    """Locate the real .git directory, including normal worktree setups."""

    result = run_command(["git", "rev-parse", "--git-dir"])
    if result.returncode == 0 and result.stdout:
        path = Path(result.stdout)
        return path if path.is_absolute() else REPO_ROOT / path
    return REPO_ROOT / ".git"


def detect_git_processes() -> tuple[list[str], str | None]:
    """Report visible Git-related Windows processes without stopping them."""

    result = run_command(["tasklist", "/fo", "csv", "/v"], timeout=20)
    if result.returncode != 0 or not result.stdout:
        return [], f"Could not inspect running processes: {result.stderr or result.stdout}"

    process_hits: list[str] = []
    target_names = {"git.exe", "githubdesktop.exe", "gh.exe", "ssh.exe"}

    reader = csv.DictReader(result.stdout.splitlines())
    for row in reader:
        image_name = (row.get("Image Name") or "").strip()
        lower_name = image_name.lower()
        window_title = (row.get("Window Title") or "").strip()

        is_credential_helper = "credential" in lower_name or "git-credential" in lower_name
        if lower_name in target_names or is_credential_helper:
            detail = image_name
            if window_title and window_title.upper() != "N/A":
                detail = f"{detail} ({window_title})"
            process_hits.append(detail)

    return sorted(set(process_hits)), None


def detect_lock_files(git_dir: Path) -> list[Path]:
    """Find Git lock files that usually mean another Git operation is active."""

    lock_files = [
        git_dir / "index.lock",
        git_dir / "HEAD.lock",
        git_dir / "config.lock",
    ]
    if (git_dir / "refs").exists():
        lock_files.extend((git_dir / "refs").rglob("*.lock"))

    return sorted(path for path in lock_files if path.exists())


def detect_unfinished_operations(git_dir: Path) -> list[str]:
    """Find marker files/directories for unfinished Git operations."""

    checks = {
        "merge in progress": [git_dir / "MERGE_HEAD"],
        "rebase in progress": [git_dir / "rebase-merge", git_dir / "rebase-apply"],
        "cherry-pick in progress": [git_dir / "CHERRY_PICK_HEAD"],
        "revert in progress": [git_dir / "REVERT_HEAD"],
        "bisect in progress": [git_dir / "BISECT_LOG"],
    }

    active: list[str] = []
    for label, paths in checks.items():
        if any(path.exists() for path in paths):
            active.append(label)
    return active


def parse_dirty_state() -> dict[str, int]:
    """Summarize git status --porcelain into useful buckets."""

    result = run_command(["git", "status", "--porcelain"])
    counts = {"staged": 0, "modified": 0, "deleted": 0, "untracked": 0}
    if result.returncode != 0:
        counts["status_error"] = 1
        return counts

    for line in result.stdout.splitlines():
        if not line:
            continue
        if line.startswith("??"):
            counts["untracked"] += 1
            continue

        staged_code = line[0]
        worktree_code = line[1] if len(line) > 1 else " "

        if staged_code != " ":
            counts["staged"] += 1
        if worktree_code == "M" or staged_code == "M":
            counts["modified"] += 1
        if worktree_code == "D" or staged_code == "D":
            counts["deleted"] += 1

    return counts


def read_branch_and_remotes() -> tuple[str, str]:
    branch = run_command(["git", "branch", "--show-current"])
    remotes = run_command(["git", "remote", "-v"])

    branch_text = branch.stdout if branch.returncode == 0 and branch.stdout else "Unknown"
    remote_text = remotes.stdout if remotes.returncode == 0 and remotes.stdout else "No remotes found"
    return branch_text, remote_text


def detect_github_connections() -> list[str]:
    """Best-effort Windows network check. This only reports; it never blocks."""

    result = run_command(["netstat", "-ano"], timeout=20)
    if result.returncode != 0 or not result.stdout:
        return []

    targets = ("github.com", "api.github.com", "ssh.github.com")
    matches: list[str] = []
    for line in result.stdout.splitlines():
        lower_line = line.lower()
        if any(target in lower_line for target in targets):
            matches.append(line.strip())
    return matches


def print_section(title: str) -> None:
    print()
    print(title)
    print("-" * len(title))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read-only Git activity preflight check for Aetherion ImageTools.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero when Git lock files or unfinished Git operations are found.",
    )
    args = parser.parse_args()

    git_dir = find_git_dir()
    print("Aetherion ImageTools Git Preflight")
    print(f"Repository: {REPO_ROOT}")
    print(f"Git dir:    {git_dir}")

    branch, remotes = read_branch_and_remotes()
    print_section("Branch And Remotes")
    print(f"Branch: {branch}")
    print(remotes)

    process_hits, process_error = detect_git_processes()
    lock_files = detect_lock_files(git_dir)
    unfinished = detect_unfinished_operations(git_dir)
    dirty = parse_dirty_state()
    connections = detect_github_connections()

    print_section("Running Git Processes")
    if process_error:
        print(f"WARN: {process_error}")
    elif process_hits:
        for process in process_hits:
            print(f"WARN: Git process running: {process}")
    else:
        print("OK: No visible Git-related process found")

    print_section("Git Lock Files")
    if lock_files:
        for lock_file in lock_files:
            print(f"WARN: Git lock file exists: {lock_file}")
    else:
        print("OK: No Git lock files found")

    print_section("Unfinished Git Operations")
    if unfinished:
        for operation in unfinished:
            print(f"WARN: {operation}")
    else:
        print("OK: No merge/rebase/cherry-pick/revert/bisect markers found")

    print_section("Dirty Repo State")
    dirty_total = sum(value for key, value in dirty.items() if key != "status_error")
    if dirty.get("status_error"):
        print("WARN: Could not read repo status")
    elif dirty_total:
        print("WARN: Repo has uncommitted changes")
        print(f"Staged files:    {dirty['staged']}")
        print(f"Modified files:  {dirty['modified']}")
        print(f"Deleted files:   {dirty['deleted']}")
        print(f"Untracked files: {dirty['untracked']}")
    else:
        print("OK: Repo is clean")

    print_section("GitHub Network Connections")
    if connections:
        for connection in connections:
            print(f"WARN: Active GitHub connection visible: {connection}")
    else:
        print("OK: No GitHub host connections visible through netstat")

    print_section("Result")
    has_activity = bool(process_hits or lock_files or unfinished or dirty_total or connections)
    if has_activity:
        if process_hits:
            print("WARN: Git process running")
        if lock_files:
            print("WARN: Git lock file exists")
        if dirty_total:
            print("WARN: Repo has uncommitted changes")
        if unfinished:
            print("WARN: Merge/rebase/cherry-pick in progress")
        if connections:
            print("WARN: GitHub network activity visible")
    else:
        print("PASS: No obvious Git activity detected")

    if args.strict and (lock_files or unfinished):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
