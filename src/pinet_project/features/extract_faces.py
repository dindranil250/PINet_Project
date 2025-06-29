# src/pinet_project/features/extract_faces.py

import os
import cv2
import torch
import logging
from facenet_pytorch import MTCNN
from PIL import Image

def extract_faces_from_frames(frame_folder: str, output_folder: str):
    os.makedirs(output_folder, exist_ok=True)

    # Set device
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    detector = MTCNN(keep_all=True, device=device)

    frame_files = sorted([
        f for f in os.listdir(frame_folder)
        if f.lower().endswith(".jpg")
    ])

    for frame_file in frame_files:
        frame_path = os.path.join(frame_folder, frame_file)

        # Load image using PIL (required by facenet-pytorch)
        image = Image.open(frame_path).convert('RGB')

        # Detect faces
        boxes, _ = detector.detect(image)

        if boxes is None:
            continue

        for i, box in enumerate(boxes):
            x1, y1, x2, y2 = map(int, box)
            cropped_face = image.crop((x1, y1, x2, y2))

            # Save face
            face_filename = f"{os.path.splitext(frame_file)[0]}_face_{i}.jpg"
            face_path = os.path.join(output_folder, face_filename)
            cropped_face.save(face_path)

    logging.info(f"Extracted faces to {output_folder}")
