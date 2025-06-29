# src/pinet_project/features/extract_audio_text.py

import os
import librosa
import soundfile as sf
import subprocess

def extract_audio_from_video(video_path, output_path_wav, sr=16000):
    """
    Extracts audio from a video file and saves it as mono .wav (16kHz) using librosa + ffmpeg.
    """
    print(f"🔊 Extracting audio from {video_path} → {output_path_wav}")

    try:
        # Step 1: Extract raw audio using ffmpeg to a temporary WAV file
        temp_wav = output_path_wav.replace(".wav", "_temp.wav")
        command = [
            "ffmpeg", "-y", "-i", video_path,
            "-vn",        # no video
            "-ac", "1",   # mono
            "-ar", str(sr),  # 16kHz sampling rate
            temp_wav
        ]
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Step 2: Load with librosa (optional — for consistency / re-saving)
        audio, _ = librosa.load(temp_wav, sr=sr, mono=True)

        # Step 3: Save clean .wav with soundfile
        sf.write(output_path_wav, audio, sr)

        # Cleanup
        os.remove(temp_wav)

        print(f"✅ Saved WAV audio: {output_path_wav}")

    except Exception as e:
        print(f"❌ Failed to extract audio from {video_path}: {e}")
