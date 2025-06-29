# src/pinet_project/features/extract_transcript.py

import whisper_timestamped
import json
import os
import logging

def transcribe_audio(audio_path: str, output_path: str, model_name="base"):
    model = whisper_timestamped.load_model(model_name)

    result = whisper_timestamped.transcribe(model, audio_path)
    if not result or "segments" not in result:
        logging.warning(f"No speech segments found in {audio_path}")
        return

    transcript_text = " ".join([seg['text'].strip() for seg in result['segments']])
    words = []
    for seg in result['segments']:
        for word in seg['words']:
            words.append({
                "word": word['text'].strip(),
                "start": round(word['start'], 2),
                "end": round(word['end'], 2)
            })

    start_time = round(words[0]['start'], 2) if words else 0.0
    end_time = round(words[-1]['end'], 2) if words else 0.0

    output = {
        "transcript": transcript_text,
        "words": words,
        "start_time": start_time,
        "end_time": end_time
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    logging.info(f"Saved transcript: {output_path}")
