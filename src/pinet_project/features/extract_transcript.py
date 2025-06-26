import whisper_timestamped
import json
import os

def transcribe_audio(audio_path, output_path):
    # Load Whisper model (use "base", "small", "medium", or "large")
    model = whisper_timestamped.load_model("base")  # or "medium" for better accuracy

    # Transcribe with timestamps
    result = whisper_timestamped.transcribe(model, audio_path)

    # Format transcript
    transcript_text = " ".join([seg['text'].strip() for seg in result['segments']])

    words = []
    for seg in result['segments']:
        for word in seg['words']:
            words.append({
                "word": word['text'].strip(),
                "start": round(word['start'], 2),
                "end": round(word['end'], 2)
            })

    # Get start and end time for the full transcript
    start_time = round(words[0]['start'], 2) if words else 0.0
    end_time = round(words[-1]['end'], 2) if words else 0.0

    # Final format
    output = {
        "transcript": transcript_text,
        "words": words,
        "start_time": start_time,
        "end_time": end_time
    }

    # Save to JSON
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Saved transcript to {output_path}")
