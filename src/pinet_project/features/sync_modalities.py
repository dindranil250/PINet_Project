# features/sync_modalities.py
import json

def load_transcript(tfile):
    with open(tfile, "r") as f:
        data = json.load(f)
    segments = data["segments"]
    return [(seg["start"], seg["end"], seg["text"]) for seg in segments]

# This will later help slice face/audio/frame sets based on same timestamp windows.
