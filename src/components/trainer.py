import pandas as pd
import numpy as np

import os 
import sys
from dataclasses import dataclass

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier,RandomForestClassifier
from sklearn.svm import SVC
from catboost import CatBoostClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

from src.logger import logging
from src.exception import CustomException

from src.components.trainsformation import DataTransformation
from src.components.evaluate import evaluate
from src.components.utils import save_object,load_object


@dataclass
class ModelTrainerConfig:
    Trainer_path=os.path.join("artificial","ModelParkinsons.pkl")


class ModelTrainer:
    def __init__(self):#بفتح المصنع 
        self.ModelTrainConfig=ModelTrainerConfig()

    def initiate_model_train(self,train_array,test_array):
        try:
            x_train, y_train = train_array[:, :-1], train_array[:, -1]
            x_test, y_test = test_array[:, :-1], test_array[:, -1]

            
            models={
                    "LogisticRegression":LogisticRegression(),
                    "tree":DecisionTreeClassifier(),
                    "knn":KNeighborsClassifier(),
                    "SVC":SVC(),
                    "XGBoost":XGBClassifier(),
                    "CatBoost":CatBoostClassifier(),
                    "RandomForest":RandomForestClassifier(),
                    "AdaBoost":AdaBoostClassifier()
            }
            params={
                    "LogisticRegression": {
                        'C': [0.01, 0.1, 1, 10],
                        'solver': ['liblinear', 'lbfgs']
                    },
                    "tree": {
                        'criterion': ['gini', 'entropy'],
                        'max_depth': [3, 5, 10, None],
                        'splitter': ['best', 'random']
                    },
                    "knn": {
                        'n_neighbors': [3, 5, 7, 9],
                        'weights': ['uniform', 'distance'],
                        'metric': ['euclidean', 'manhattan']
                    },
                    "SVC": {
                        'C': [0.1, 1, 10],
                        'kernel': ['linear', 'rbf', 'poly'],
                        'gamma': ['scale', 'auto']
                    },
                    "XGBoost": {
                        'n_estimators': [50, 100, 200],
                        'learning_rate': [0.01, 0.1, 0.2],
                        'max_depth': [3, 5, 7]
                    },
                    "CatBoost": {
                        'iterations': [50, 100],
                        'depth': [4, 6, 8],
                        'learning_rate': [0.01, 0.1]
                    },
                    "RandomForest": {
                        'n_estimators': [50, 100, 200],
                        'max_features': ['sqrt', 'log2'],
                        'criterion': ['gini', 'entropy']
                    },
                    "AdaBoost": {
                        'n_estimators': [50, 100, 200],
                        'learning_rate': [0.01, 0.1, 1]
                    }

            }
            #evaluate
            model_report = evaluate(x_train, y_train, x_test, y_test, params=params, models=models)

            #select the best model
            best_model_name = max(model_report, key=lambda x: model_report[x]['f1'])
            best_model = model_report[best_model_name]["best_model"]


            if model_report[best_model_name]["f1"] < 0.6:
                    raise CustomException("Not found Best Model")
            
            
                #save
            save_object(
                    file_path=self.ModelTrainConfig.Trainer_path,
                    obj=best_model
                )
            

            predict=best_model.predict(x_test)
            accuracy=accuracy_score(y_test,predict)
            return accuracy



        except Exception as e:
            raise CustomException(e,sys)