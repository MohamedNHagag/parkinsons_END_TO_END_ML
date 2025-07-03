
import os 
import sys

import pandas as pd

from src.exception import CustomException
from src.components.utils import save_object
from src.components.utils import load_object

#دخل حول لخصائص وبعد كدا حول لداتا فريم
class custmerdata:
    def __init__(self,
                MDVP_Fo_Hz: float,
                MDVP_Fhi_Hz: float,
                MDVP_Flo_Hz: float,
                MDVP_Jitter_percent: float,
                MDVP_Jitter_Abs: float,
                MDVP_RAP: float,
                MDVP_PPQ: float,
                Jitter_DDP: float,
                MDVP_Shimmer: float,
                MDVP_Shimmer_dB: float,
                Shimmer_APQ3: float,
                Shimmer_APQ5: float,
                MDVP_APQ: float,
                Shimmer_DDA: float,
                NHR: float,
                HNR: float,
                RPDE: float,
                DFA: float,
                spread1: float,
                spread2: float,
                D2: float,
                PPE: float):
                            self.MDVP_Fo_Hz = MDVP_Fo_Hz
                            self.MDVP_Fhi_Hz = MDVP_Fhi_Hz
                            self.MDVP_Flo_Hz = MDVP_Flo_Hz
                            self.MDVP_Jitter_percent = MDVP_Jitter_percent
                            self.MDVP_Jitter_Abs = MDVP_Jitter_Abs
                            self.MDVP_RAP = MDVP_RAP
                            self.MDVP_PPQ = MDVP_PPQ
                            self.Jitter_DDP = Jitter_DDP
                            self.MDVP_Shimmer = MDVP_Shimmer
                            self.MDVP_Shimmer_dB = MDVP_Shimmer_dB
                            self.Shimmer_APQ3 = Shimmer_APQ3
                            self.Shimmer_APQ5 = Shimmer_APQ5
                            self.MDVP_APQ = MDVP_APQ
                            self.Shimmer_DDA = Shimmer_DDA
                            self.NHR = NHR
                            self.HNR = HNR
                            self.RPDE = RPDE
                            self.DFA = DFA
                            self.spread1 = spread1
                            self.spread2 = spread2
                            self.D2 = D2
                            self.PPE = PPE    

    def get_data_to_dataframe(self):
        try:
            data_dict = {
                "MDVP:Fo(Hz)": [self.MDVP_Fo_Hz],
                "MDVP:Fhi(Hz)": [self.MDVP_Fhi_Hz],
                "MDVP:Flo(Hz)": [self.MDVP_Flo_Hz],
                "MDVP:Jitter(%)": [self.MDVP_Jitter_percent],
                "MDVP:Jitter(Abs)": [self.MDVP_Jitter_Abs],
                "MDVP:RAP": [self.MDVP_RAP],
                "MDVP:PPQ": [self.MDVP_PPQ],
                "Jitter:DDP": [self.Jitter_DDP],
                "MDVP:Shimmer": [self.MDVP_Shimmer],
                "MDVP:Shimmer(dB)": [self.MDVP_Shimmer_dB],
                "Shimmer:APQ3": [self.Shimmer_APQ3],
                "Shimmer:APQ5": [self.Shimmer_APQ5],
                "MDVP:APQ": [self.MDVP_APQ],
                "Shimmer:DDA": [self.Shimmer_DDA],
                "NHR": [self.NHR],
                "HNR": [self.HNR],
                "RPDE": [self.RPDE],
                "DFA": [self.DFA],
                "spread1": [self.spread1],
                "spread2": [self.spread2],
                "D2": [self.D2],
                "PPE": [self.PPE],
            }
            return pd.DataFrame(data_dict)
        except Exception as e:
            raise CustomException(e, sys)    
        



class predictionpipeline:#✅ prepare data and predict
    def __init__(self):
        pass
    def predict(self,feature):
        try:
            #get path objects
            Model_path=os.path.join("artificial","ModelParkinsons.pkl")
            preprocessing_path=os.path.join("artificial","preprocessor.pkl")

            #load
            model=load_object(file_path=Model_path)
            preprocessing=load_object(file_path=preprocessing_path)
            #work preproccing and predict
            data_scaled=preprocessing.transform(feature)
            predicts=model.predict(data_scaled)

            return predicts
        except Exception as e:
            raise CustomException(e,sys)