import os
from pathlib import Path
from src.logger import logging
from datetime import datetime

# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
# os.makedirs(logs_path, exist_ok = True)

# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    # filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,

)

project_name = "CNN_Classifier"

list_of_files = [
    ".github/workflows/.gitkeep" ##create gitkeep to keep file when commit
    "src/__init__.py",
    "src/exception.py",
    "src/logger.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/config/configuration.py",
    "src/pipeline/__init__.py",
    "src/entity/__init__.py",
    "src/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath) ## Convert to Window path using backslash
    filedir, filename = os.path.split(filepath)

    if (filedir != "") and (not os.path.exists(filedir)):
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")
        
    else:
        logging.info(f"{filename} is already exist")