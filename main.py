
import sys
from src.components.ingestion import DataIngestion
from src.components.trainsformation import DataTransformation
from src.components.trainer import ModelTrainer
from src.logger import logging
from src.exception import CustomException

if __name__ == "__main__":
    try:
        logging.info("Start Data Ingestion Step")
        #هات اوبجيكت
        ingestion_obj = DataIngestion()
        #طبق علي الديف بتاع initate تلك الاوبجيكت
        train_path, test_path = ingestion_obj.Initiate_data_ingestion()


        logging.info("Start Data Transformation Step")
        #هات اوبجيكت
        transformation_obj = DataTransformation()
        #طبق علي الديف بتاع initate تلك الاوبجيكت
        train_arr, test_arr, _ = transformation_obj.initiate_data_transformation(train_path, test_path)

        logging.info("Start Model Training Step")
        #هات اوبجيكت
        model_obj = ModelTrainer()
        #طبق علي الديف بتاع initate تلك الاوبجيكت
        accuracy = model_obj.initiate_model_train(train_arr, test_arr)

        #النتيجه
        print(f"✅ Model Trained Successfully with Accuracy: {accuracy}")
        logging.info(f"✅ Model Trained Successfully with Accuracy: {accuracy}")

    except Exception as e:
        logging.error(f"❌ Error occurred: {str(e)}")
        raise CustomException(e, sys)


