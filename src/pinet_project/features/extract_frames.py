# src/pinet_project/features/extract_frames.py

import cv2
import os
import logging

def extract_frames(video_path: str, output_folder: str, every_n_frames: int = 5):
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % every_n_frames == 0:
            frame_filename = f"frame_{saved_count:04d}.jpg"
            cv2.imwrite(os.path.join(output_folder, frame_filename), frame)
            saved_count += 1
        frame_count += 1

    cap.release()
    logging.info(f"Saved {saved_count} frames to {output_folder}")
