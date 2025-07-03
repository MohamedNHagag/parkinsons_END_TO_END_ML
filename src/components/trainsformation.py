import numpy as np
import os
from dataclasses import dataclass
import sys
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.components.utils import save_object,load_object

from src.components.ingestion import DataIngestion
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer 





@dataclass
class DataTransformationConfig:
    preprocessor_file_path = os.path.join("artificial", "Transformation", "preprocessor.pkl")






class DataTransformation:

    def __init__(self):
        self.Transformationconfig = DataTransformationConfig()

    def get_data_transform(self):
            try:
                features = [
                    'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 
                    'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 
                    'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 
                    'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
                ]
                
                num_pipeline = Pipeline(steps=[
                    ("scaler", StandardScaler())
                ])
                
                preprocessor= ColumnTransformer(transformers=[
                    ("num_pipeline", num_pipeline, features)
                ])       

                return preprocessor
            
            except Exception as e:
                raise CustomException(e, sys)




    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            preprocessor_obj = self.get_data_transform()
            
            features = [
                    'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 
                    'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 
                    'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 
                    'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
                ]
            target = "status"
            input_train = train_df[features]
            target_train = train_df[target]

            input_test = test_df[features]
            target_test = test_df[target]

            input_train_arr = preprocessor_obj.fit_transform(input_train)
            input_test_arr = preprocessor_obj.transform(input_test)
            
            train_arr = np.c_[input_train_arr, np.array(target_train)]
            test_arr = np.c_[input_test_arr, np.array(target_test)]

            save_object(
                file_path=self.Transformationconfig.preprocessor_file_path,
                obj=preprocessor_obj
            )

            return train_arr, test_arr, self.Transformationconfig.preprocessor_file_path

        except Exception as e:
            raise CustomException(e, sys)
        

