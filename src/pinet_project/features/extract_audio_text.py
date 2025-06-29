# src/pinet_project/features/extract_audio_text.py

import os
from moviepy import VideoFileClip
import logging

def extract_audio_from_video(video_path: str, output_audio_path: str):
    os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)

    try:
        clip = VideoFileClip(video_path)
        if clip.audio is None:
            logging.warning(f"No audio found in {video_path}")
            return
        clip.audio.write_audiofile(output_audio_path, logger=None)
        clip.close()
        logging.info(f"Extracted audio to {output_audio_path}")
    except Exception as e:
        logging.error(f"Failed to extract audio from {video_path}: {e}")
