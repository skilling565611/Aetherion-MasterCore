from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


BITRATE_STEPS_KBPS = (128, 112, 96, 80, 64, 48, 40, 32)
TEXT_TAGS = ("lyrics", "unsyncedlyrics", "syncedlyrics", "comment", "description")


def run_command(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, check=True, capture_output=True, text=True)


def require_tool(name: str) -> None:
    if shutil.which(name) is None:
        raise SystemExit(f"Missing required tool: {name}. Install ffmpeg and add it to PATH.")


def file_size(path: Path) -> int:
    return path.stat().st_size


def mb_to_bytes(value: float) -> int:
    return int(value * 1024 * 1024)


def probe_duration_seconds(path: Path) -> float:
    result = run_command(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(path),
        ]
    )
    payload = json.loads(result.stdout)
    duration = payload.get("format", {}).get("duration")
    if duration is None:
        raise SystemExit(f"Could not read duration from {path}")
    return float(duration)


def probe_format_tags(path: Path) -> dict[str, str]:
    result = run_command(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format_tags",
            "-of",
            "json",
            str(path),
        ]
    )
    payload = json.loads(result.stdout)
    tags = payload.get("format", {}).get("tags", {})
    return {str(key).lower(): str(value) for key, value in tags.items()}


def build_text_sidecar(input_path: Path, output_path: Path, audio_output_path: Path) -> None:
    tags = probe_format_tags(input_path)
    extracted_lines: list[str] = []

    for tag_name in TEXT_TAGS:
        value = tags.get(tag_name)
        if value:
            extracted_lines.append(f"[{tag_name}]")
            extracted_lines.append(value.strip())
            extracted_lines.append("")

    if not extracted_lines:
        extracted_lines = [
            "[title]",
            input_path.stem,
            "",
            "[source audio]",
            str(input_path),
            "",
            "[edited audio]",
            str(audio_output_path),
            "",
            "[lyrics]",
            "",
            "[verse 1]",
            "",
            "[pre-chorus]",
            "",
            "[chorus]",
            "",
            "[verse 2]",
            "",
            "[bridge]",
            "",
            "[background sounds]",
            "",
            "[notes]",
            "",
        ]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(extracted_lines).rstrip() + "\n", encoding="utf-8")


def encode_audio(input_path: Path, output_path: Path, bitrate_kbps: int, trim_seconds: float | None) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    command = [
        "ffmpeg",
        "-y",
        "-i",
        str(input_path),
        "-vn",
        "-map_metadata",
        "-1",
        "-ac",
        "2",
        "-ar",
        "44100",
        "-b:a",
        f"{bitrate_kbps}k",
    ]

    if trim_seconds is not None:
        command.extend(["-t", f"{trim_seconds:.3f}"])

    command.append(str(output_path))
    run_command(command)


def fit_audio(input_path: Path, output_path: Path, max_bytes: int) -> tuple[int, float | None]:
    if not input_path.exists():
        raise SystemExit(f"Input file does not exist: {input_path}")

    original_duration = probe_duration_seconds(input_path)

    for bitrate in BITRATE_STEPS_KBPS:
        encode_audio(input_path, output_path, bitrate, None)
        if file_size(output_path) <= max_bytes:
            return bitrate, None

    bitrate = BITRATE_STEPS_KBPS[-1]
    trim_seconds = original_duration

    for _ in range(8):
        current_size = file_size(output_path)
        if current_size <= max_bytes:
            return bitrate, trim_seconds

        ratio = max_bytes / current_size
        trim_seconds = max(1.0, trim_seconds * ratio * 0.97)
        encode_audio(input_path, output_path, bitrate, trim_seconds)

    if file_size(output_path) > max_bytes:
        size_mb = file_size(output_path) / 1024 / 1024
        max_mb = max_bytes / 1024 / 1024
        raise SystemExit(f"Could not fit output under {max_mb:.2f} MB. Final size: {size_mb:.2f} MB.")

    return bitrate, trim_seconds


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compress and trim audio to fit under a target file size.")
    parser.add_argument("input", type=Path, help="Raw source audio file, usually from Suno.")
    parser.add_argument("output", type=Path, help="Edited output audio file for chatbot upload.")
    parser.add_argument("--max-mb", type=float, default=4.9, help="Maximum output size in MB. Default: 4.9")
    parser.add_argument(
        "--text-output",
        type=Path,
        help="Optional text sidecar path for embedded lyrics/comments or a fill-in lyrics and background notes template.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    require_tool("ffmpeg")
    require_tool("ffprobe")

    max_bytes = mb_to_bytes(args.max_mb)
    bitrate, trim_seconds = fit_audio(args.input, args.output, max_bytes)
    if args.text_output:
        build_text_sidecar(args.input, args.text_output, args.output)

    output_mb = file_size(args.output) / 1024 / 1024

    print(f"Created: {args.output}")
    print(f"Size: {output_mb:.2f} MB")
    print(f"Bitrate: {bitrate} kbps")
    if trim_seconds is not None:
        print(f"Trimmed duration: {trim_seconds:.2f} seconds")
    else:
        print("Trimmed duration: none")
    if args.text_output:
        print(f"Text sidecar: {args.text_output}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
