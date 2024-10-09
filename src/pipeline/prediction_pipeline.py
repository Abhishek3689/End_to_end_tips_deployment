from src.utils import load_object
import pandas as pd
import os,sys
from sklearn.metrics import r2_score
from src.logger import logging
from src.exception import CustomException



class CustomData:
    def __init__(self,
                 sex:str,
                 smoker:str,
                 day:str,
                 time:str,
                 total_bill:float,
                 size:int):
        self.sex=sex
        self.smoker=smoker
        self.day=day
        self.time=time
        self.total_bill=total_bill
        self.size=size
    
    def get_custom_data_as_frame(self):
        try:
            logging.info("Getting input features into dataframe")
            custom_dict={
                "total_bill":[self.total_bill],
                "size":[self.size],
                "sex":[self.sex],
                "smoker":[self.smoker],
                "day":[self.day],
                "time":[self.time]
                
            }

            df_feature=pd.DataFrame(custom_dict)

            return df_feature
        except Exception as e:
            raise CustomException(e,sys)
        

class Prediction_Pipeline:
    def __init__(self):
        pass

    def predict(self,features):
        preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
        model_path=os.path.join('artifacts','model.pkl')

        logging.info("Loading model and preprocessor")
        preprocessor=load_object(preprocessor_path)
        model=load_object(model_path)
        scaled_feature=preprocessor.transform(features)
        y_pred=model.predict(scaled_feature)
        return y_pred
    