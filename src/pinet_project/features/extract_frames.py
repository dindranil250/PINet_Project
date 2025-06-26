import cv2
import os

def extract_frames(video_path: str, output_dir: str, frame_rate: int = 1):
    """
    Extract frames from a video every `frame_rate` seconds.
    """
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * frame_rate)
    frame_count = 0
    saved_frame_idx = 0

    while True:
        success, frame = cap.read()
        if not success:
            break
        if frame_count % frame_interval == 0:
            frame_name = f"frame_{saved_frame_idx:04d}.jpg"
            frame_path = os.path.join(output_dir, frame_name)
            cv2.imwrite(frame_path, frame)
            saved_frame_idx += 1
        frame_count += 1

    cap.release()
