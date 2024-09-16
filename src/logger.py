import logging
import os
from datetime import datetime

LOG_FOLDER = f"{datetime.now().strftime('%m_%d_%Y')}"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FOLDER)

if not os.path.exists(logs_path):
    os.makedirs(logs_path, exist_ok = True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(module)s - %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,

)

