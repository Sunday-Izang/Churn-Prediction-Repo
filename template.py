import os
from pathlib import Path
import logging

logging.basicConfig(level =logging.INFO, format ='[%(asctime)s]: %(message)s:')

project_name = "CCPredictor"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/data/__init__.py",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/images/__init__.py",
    f"src/{project_name}/reports/__init__.py",
    f"src/{project_name}/notebooks/__init__.py",
    f"src/{project_name}/static/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "docs.docx",
    "app.py",
    "LICENSE"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")