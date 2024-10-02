from src.utils.utils import copy_random_imgfiles
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
import os
import sys


# Extract random image data for training and testing from source directory

@dataclass
class DataIngestionConfig:
    src_path: str = "Bottle Images"
    dest_path: str = os.path.join("artifacts","raw_img")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def save_random_img(self, num_img: int):
        try:
            if not os.path.isdir(os.path.join(self.ingestion_config.dest_path)):
                copy_random_imgfiles(src_dir= self.ingestion_config.src_path, dest_dir=self.ingestion_config.dest_path, num_img=num_img)
                logging.info(f"{num_img} image files are collected and saved")
            else:
                logging.info("image files are already saved")
        
        except Exception as e:
            raise CustomException(e, sys)


# if __name__ == "__main__":
    
#     data_ingestion = DataIngestion()
#     data_ingestion.get_random_img(5)