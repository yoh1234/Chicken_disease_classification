from src.components.data_ingestion import DataIngestion


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
    
        data_ingestion = DataIngestion()
        data_ingestion.save_random_img(500)