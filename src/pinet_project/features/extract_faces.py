from mtcnn import MTCNN
import cv2
import os

def extract_faces_from_frames(frame_dir: str, output_dir: str):
    """
    Detects faces in each frame and saves cropped face images.
    """
    os.makedirs(output_dir, exist_ok=True)
    detector = MTCNN()

    for frame_file in sorted(os.listdir(frame_dir)):
        if not frame_file.endswith(".jpg"):
            continue
        frame_path = os.path.join(frame_dir, frame_file)
        img = cv2.imread(frame_path)
        result = detector.detect_faces(img)

        for i, face in enumerate(result):
            x, y, width, height = face['box']
            x, y = max(0, x), max(0, y)
            face_img = img[y:y+height, x:x+width]
            face_filename = f"{os.path.splitext(frame_file)[0]}_face_{i:02d}.jpg"
            face_path = os.path.join(output_dir, face_filename)
            cv2.imwrite(face_path, face_img)
