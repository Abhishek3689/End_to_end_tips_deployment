import os,sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from src.components.data_transformation import DataTransform
from dataclasses import dataclass
from src.utils import evaluate_model,save_object
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor

@dataclass
class ModelTrainerConfig:
    model_path=os.path.join('artifacts','model.pkl')
    train_data_path=os.path.join("artifiacts","train.csv")
    test_data_path=os.path.join("artifiacts","test.csv")

class ModelTrainer(ModelTrainerConfig):
    def __init__(self):
        self.model_config=ModelTrainerConfig()



    def initiate_model_training(self,df_train_scaled,df_test_scaled):
        try:
            logging.info("Model trainer started ")
            logging.info("seperating input and outpu feature")
            X_train_scaled=df_train_scaled[:,:-1]
            y_train=df_train_scaled[:,-1]
            X_test_scaled=df_test_scaled[:,:-1]
            y_test=df_test_scaled[:,-1]
            # train_data=pd.read_csv(self.model_config.train_data_path)
            # y_train=train_data['tip']
            # test_data=pd.read_csv(self.model_config.test_data_path)
            # y_test=test_data['tip']
            logging.info("making a dictionary of differnt model algorithms to be trained ")
            models={
            'Decisiontree':DecisionTreeRegressor(),
            'RandomForest':RandomForestRegressor(),
            'LinearRegressor':LinearRegression(),
            'AdaBoost':AdaBoostRegressor()
            }
          
            report=evaluate_model(X_train_scaled,X_test_scaled,y_train,y_test,models)
            best_model_name=max(report.items(),key=lambda x:x[1])
            logging.info(f"Best model is found to be {[best_model_name[0]]} and best score is {[best_model_name[1]]}")
            best_model=models[best_model_name[0]]

            save_object(self.model_config.model_path,best_model)
            logging.info("Model trainer finished and best Model have been saved")
        except Exception as e:
            raise CustomException(e,sys)

