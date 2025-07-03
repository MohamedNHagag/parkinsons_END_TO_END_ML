import os 
import sys
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException

import pandas as pd
from sklearn.model_selection import train_test_split



@dataclass
class IngestionDataConfig:
    train_data:str=os.path.join("artificial","train.csv")
    test_data:str=os.path.join("artificial","test.csv")
    raw_data:str=os.path.join("artificial","data.csv")


class DataIngestion:
    def __init__(self):
        self.IngestionConfig=IngestionDataConfig()

    
    def Initiate_data_ingestion(self):
        try:
            df=pd.read_csv(r'D:\Data_Science\7-Machine_Learning\projects\END-TO-END_projectsML\parkinsons_END_TO_END_ML\NoteBook\Dataset\parkinsons.data')
            os.makedirs(os.path.dirname(self.IngestionConfig.train_data),exist_ok=True)
            df.to_csv(self.IngestionConfig.raw_data,index=False,header=True)

            train_set,test_set=train_test_split(df,random_state=42,test_size=0.1)
            train_set.to_csv(self.IngestionConfig.train_data,index=False,header=True)
            test_set.to_csv(self.IngestionConfig.test_data,index=False,header=True)


            return(self.IngestionConfig.train_data,self.IngestionConfig.test_data)
        

        except Exception as e:
            raise CustomException(e,sys)
        


