from src.exception import CustomException
from src.logger import logging
from src.components.prepare_model import PrepareBaseCnnModel
import sys

class PrepareModelPipeline:
    def __init__(self):
        pass

    def main(self):
    
        try:
            CNN_model = PrepareBaseCnnModel()
            CNN_model.prepare_full_cnn_model(freeze_all=True)
        except Exception as e:
            raise CustomException(e, sys)
        
