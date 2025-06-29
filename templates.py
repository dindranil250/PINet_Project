import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")

project_name = "pinet_project"

list_of_files = [
    # Config
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/config/default.yaml",

    # Data folders
    f"src/{project_name}/data/raw_videos/.gitkeep",
    f"src/{project_name}/data/preprocessed/.gitkeep",
    f"src/{project_name}/data/annotations/.gitkeep",

    # Dataset
    f"src/{project_name}/datasets/__init__.py",
    f"src/{project_name}/datasets/prepare_dataset.py",
    

    # Feature Extraction
    f"src/{project_name}/features/__init__.py",
    f"src/{project_name}/features/extract_faces.py",
    f"src/{project_name}/features/extract_audio_text.py",
    f"src/{project_name}/features/extract_frames.py",
    f"src/{project_name}/features/extract_transcript.py",
    f"src/{project_name}/features/sync_modalities.py",

    # Models
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/models/pinet.py",
    f"src/{project_name}/models/mfa.py",
    f"src/{project_name}/models/mfi.py",
    f"src/{project_name}/models/loss.py",

    # Main scripts
    f"src/{project_name}/train.py",
    f"src/{project_name}/eval.py",
    f"src/{project_name}/inference.py",

    # Utilities
    
    f"src/{project_name}/utils/metrics.py",
    f"src/{project_name}/utils/visualize.py",



    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent

    # Create directories if they don't exist
    if not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {filedir}")

    # Create the file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            if filepath.suffix == ".py":
                f.write("# " + filepath.name)
            elif filepath.suffix == ".sh":
                f.write("#!/bin/bash\n")
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
