import os 
from pathlib import Path 
import logging


logging.basicConfig(level=logging.INFO, format="[%(asctime)s]:%(message)s:")


list = [
    f"src/__init__.py",
    f"src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trails.ipynb",
]

for filepath in list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file: {filename}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)  == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creatign empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists") 