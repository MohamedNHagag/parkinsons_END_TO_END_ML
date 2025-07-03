import sys
import os
import pandas as pd
import numpy as np


from sklearn.model_selection import RandomizedSearchCV,GridSearchCV
from sklearn.metrics import accuracy_score,f1_score,classification_report

from src.logger import logging
from src.exception import CustomException


def evaluate(x_train,y_train,x_test,y_test,params:dict,models:dict):
    try:
            evaluate_model = {}
            for name,obj_model in models.items():
                if name in params and params[name]:
                    RandomizedSearch=RandomizedSearchCV(
                        estimator=obj_model,
                        param_distributions=params[name],
                        n_iter=10,
                        cv=5,
                        verbose=0,
                        random_state=42,
                        n_jobs=-1
                        )
                    RandomizedSearch.fit(x_train,y_train)
                    best_model=RandomizedSearch.best_estimator_

                else:
                    best_model=obj_model
                    best_model.fit(x_train,y_train)

                predict=best_model.predict(x_test)


                accuracy=accuracy_score(y_test,predict)
                f1=f1_score(y_test,predict)
                report=classification_report(y_test,predict)


                evaluate_model[name]={
                    "best_model":best_model,
                    "accuracy":accuracy,
                    "f1":f1,
                    "report":report
                }

            return evaluate_model


    except Exception as e:
        raise CustomException(e,sys)
    