# AI Audio Tools

Small local tools for preparing audio files for AI chatbot uploads.

The main target is a chatbot-safe edited audio file under 5 MB. The script keeps the raw Suno export separate from the compressed or trimmed output.

## Folder Flow

Raw Suno file:

```text
AI/Perchance/AUDIO/Nyra Vale/Suno Raw/
```

Edited chatbot-ready file:

```text
AI/Perchance/AUDIO/Nyra Vale/Suno Edited/
```

## Requirement

Install `ffmpeg` and make sure `ffmpeg` and `ffprobe` are available in your terminal path.

Python is set up locally for this tool:

```text
AI/AudioTools/.python-runtime/
AI/AudioTools/.venv/
```

Those folders are ignored by git. The user PATH has also been updated to include:

```text
D:\Aetherion-MasterCore\AI\AudioTools\.venv\Scripts
D:\Aetherion-MasterCore\AI\AudioTools\.python-runtime\tools
```

Use the venv Python directly when you want the most reliable command:

```powershell
AI/AudioTools/.venv/Scripts/python.exe AI/AudioTools/scripts/fit_audio.py input.mp3 output.mp3
```

## Usage

```powershell
python AI/AudioTools/scripts/fit_audio.py `
  "AI/Perchance/AUDIO/Nyra Vale/Suno Raw/song.mp3" `
  "AI/Perchance/AUDIO/Nyra Vale/Suno Edited/song_chatbot.mp3"
```

By default, the output target is 4.9 MB so the file stays just under the picky 5 MB limit. The script tries lower audio bitrates first. If the file is still too large, it trims the end until the output fits.

To change the target:

```powershell
python AI/AudioTools/scripts/fit_audio.py input.mp3 output.mp3 --max-mb 4.8
```

## Text Sidecar

The script can also create a small `.txt` file for lyrics, section labels, and background sound notes:

```powershell
python AI/AudioTools/scripts/fit_audio.py `
  "AI/Perchance/AUDIO/Nyra Vale/Suno Raw/song.mp3" `
  "AI/Perchance/AUDIO/Nyra Vale/Suno Edited/song_chatbot.mp3" `
  --text-output "AI/Perchance/AUDIO/Nyra Vale/Suno Edited/song_chatbot.txt"
```

If the Suno export has embedded lyrics or comments, the script copies those into the text file. If not, it creates a fill-in template with separate sections for verse, pre-chorus, chorus, bridge, background sounds, and notes.

This does not use internet transcription. It only reads local audio metadata and creates a clean local text file.
