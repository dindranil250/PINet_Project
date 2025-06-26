import os
from moviepy.editor import VideoFileClip

# Input and output folder paths
video_folder = "videos"
audio_folder = "audios"

# Create the audios folder if it doesn't exist
os.makedirs(audio_folder, exist_ok=True)

# Loop through all files in the video folder
for filename in os.listdir(video_folder):
    if filename.lower().endswith((".mp4", ".mkv", ".avi", ".mov", ".webm")):
        video_path = os.path.join(video_folder, filename)
        audio_filename = os.path.splitext(filename)[0] + "_audio.mp3"
        audio_path = os.path.join(audio_folder, audio_filename)

        try:
            print(f"Processing: {filename}")
            clip = VideoFileClip(video_path)
            clip.audio.write_audiofile(audio_path, logger=None)
            clip.close()
            print(f"Saved audio: {audio_path}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
