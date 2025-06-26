# src/pinet_project/app.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from src.pinet_project.datasets.prepare_dataset import main as run_prepare_dataset
from src.pinet_project.logger import logging

# Toggle this to True/False manually
RUN_DATASET_PREPARATION = True

if __name__ == "__main__":
    logging.info("App started.")

    if RUN_DATASET_PREPARATION:
        logging.info("Running dataset preparation...")
        run_prepare_dataset()
        logging.info("Dataset preparation completed.")
    else:
        logging.info("Skipped dataset preparation.")

    logging.info("App finished.")
