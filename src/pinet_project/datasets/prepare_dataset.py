# src/pinet_project/scripts/prepare_dataset.py

import os
from glob import glob
from pathlib import Path
from pinet_project.features.extract_audio_text import extract_audio_from_video
from pinet_project.features.extract_transcript import transcribe_audio
from pinet_project.logger import logging
from pinet_project.features.extract_frames import extract_frames
from pinet_project.features.extract_faces import extract_faces_from_frames


RAW_VIDEOS_DIR = "src/pinet_project/data/raw_videos"
PREPROCESSED_DIR = "src/pinet_project/data/preprocessed"

def process_video(video_path: str):
    video_name = Path(video_path).stem  # e.g., P001_Q01
    sample_dir = os.path.join(PREPROCESSED_DIR, video_name)
    audio_path = os.path.join(sample_dir, "audio", f"{video_name}_audio.wav")
    transcript_path = os.path.join(sample_dir, "text", f"{video_name}_transcript.json")
    frame_dir = os.path.join(sample_dir, "frame")
    # Step 4: Extract Faces from Frames
    face_dir = os.path.join(sample_dir, "face")
    

    try:
        logging.info(f"Processing {video_name}")
         # Step 1: Extract Audio
        print("🔊 Extracting audio...")
        extract_audio_from_video(video_path, audio_path)
        # Step 2: Transcribe Audio
        print("📝 Transcribing audio...")
        transcribe_audio(audio_path, transcript_path)
        # Step 3: Extract Frames
        print("🖼️ Extracting frames...")
        extract_frames(video_path, frame_dir)
        # Step 4: Extract Faces
        print("😃 Detecting faces...")
        extract_faces_from_frames(frame_dir, face_dir)
        logging.info(f"Completed {video_name}")
    except Exception as e:
        logging.error(f"Failed to process {video_name}: {e}")

def main():
    video_files = glob(os.path.join(RAW_VIDEOS_DIR, "*.mp4"))
    logging.info(f"Found {len(video_files)} video files.")
    for video_path in video_files:
        process_video(video_path)

if __name__ == "__main__":
    main()
