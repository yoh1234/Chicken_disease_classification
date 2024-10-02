from src.logger import logging
from src.exception import CustomException
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_prepare_model import PrepareModelPipeline
import sys

# STAGE_NAME = "Data Ingestion Stage" 
# try:
#     logging.info(f">>>>>>>>>> stage 01: {STAGE_NAME} started <<<<<<<<<<")
#     data_ingestion = DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logging.info(f">>>>>>>>>> stage 01: {STAGE_NAME} completed <<<<<<<<<<")

# except Exception as e:
#     raise CustomException(e, sys)

STAGE_NAME = "Prepare transfered CNN model"
try:
    logging.info(f">>>>>>>>>> stage 02: {STAGE_NAME} started <<<<<<<<<<")
    transfered_cnn_model = PrepareModelPipeline()
    transfered_cnn_model.main()
    logging.info(f">>>>>>>>>> stage 02: {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    raise CustomException(e, sys)
