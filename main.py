from src.logger import logging
from src.exception import CustomException
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
import sys

STAGE_NAME = "Data Ingestion Stage" 
try:
    logging.info(f">>>>>>>>>> stage 01: {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>>>>>>>>> stage 01: {STAGE_NAME} completed <<<<<<<<<<")

except Exception as e:
    raise CustomException(e, sys)