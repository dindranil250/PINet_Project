# test_preprocessing.py

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from pinet_project.features.extract_audio_text import extract_audio_from_video
from pinet_project.features.extract_transcript import transcribe_audio
from pinet_project.features.extract_frames import extract_frames
from pinet_project.features.extract_faces import extract_faces_from_frames

from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")

# Sample test video
VIDEO_PATH = "src/pinet_project/data/raw_videos/5b214ff965753400017af117_q1_generic.mp4"
VIDEO_NAME = Path(VIDEO_PATH).stem
BASE_DIR = f"src/pinet_project/data/preprocessed/{VIDEO_NAME}"

AUDIO_PATH = os.path.join(BASE_DIR, "audio", f"{VIDEO_NAME}_audio.wav")
TRANSCRIPT_PATH = os.path.join(BASE_DIR, "text", f"{VIDEO_NAME}_transcript.json")
FRAME_DIR = os.path.join(BASE_DIR, "frame")
FACE_DIR = os.path.join(BASE_DIR, "face")

def run_all_tests():
    # Ensure directories exist
    os.makedirs(os.path.dirname(AUDIO_PATH), exist_ok=True)
    os.makedirs(os.path.dirname(TRANSCRIPT_PATH), exist_ok=True)
    os.makedirs(FRAME_DIR, exist_ok=True)
    os.makedirs(FACE_DIR, exist_ok=True)

    print("\n🧪 Running test pipeline on:", VIDEO_PATH)

    # Step 1: Extract Audio
    print("🔊 Extracting audio...")
    extract_audio_from_video(VIDEO_PATH, AUDIO_PATH)
    assert os.path.exists(AUDIO_PATH), "❌ Audio file was not created."

    # Step 2: Transcribe Audio
    print("📝 Transcribing audio...")
    transcribe_audio(AUDIO_PATH, TRANSCRIPT_PATH)
    assert os.path.exists(TRANSCRIPT_PATH), "❌ Transcript file was not created."

    # Step 3: Extract Frames
    print("🖼️ Extracting frames...")
    extract_frames(VIDEO_PATH, FRAME_DIR)
    assert any(f.endswith(".jpg") for f in os.listdir(FRAME_DIR)), "❌ No frames extracted."

    # Step 4: Extract Faces
    print("😃 Detecting faces...")
    extract_faces_from_frames(FRAME_DIR, FACE_DIR)
    if not any(f.endswith(".jpg") for f in os.listdir(FACE_DIR)):
        print("⚠️  No faces detected. Try a different video with visible faces.")
    else:
        print("✅ Faces extracted!")

    print("\n🎉 All steps completed.\n")

if __name__ == "__main__":
    run_all_tests()
