import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException




#"حط الحاجة دي في الشنطة، وخزّنها في المكان دا على الجهاز"
def save_object(file_path, obj): #save object to use later
    try:
        dir_path = os.path.dirname(file_path) 
        os.makedirs(dir_path, exist_ok=True)
        #open file and save 
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)


    except Exception as e:
        raise CustomException(e, sys)
    






def load_object(file_path):#load object Pre-saved in this path
    try:
        #open file and load
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj) 

    except Exception as e:
        raise CustomException(e, sys)
    