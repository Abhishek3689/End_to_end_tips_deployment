import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.utils import save_object

@dataclass
class DataTransformConfig:
    preprocessor_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransform:
    def __init__(self):
        self.transform_config=DataTransformConfig()
        
    def get_tranform_data_object(self):
        try:
            logging.info("selecting numerial and categorical columns to get preprocessor object" )
            num_col=['total_bill', 'size']
            cat_col=['sex', 'smoker', 'day', 'time']

            logging.info("Applying numerical and categorical pipeline")
            num_pipeline=Pipeline([
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())
            ])

            cat_pipeline=Pipeline([
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('Encoder',OneHotEncoder())
            ])

            logging.info("building a preprocesor object")
            preprocessor=ColumnTransformer([
                ('numerical_pipleine',num_pipeline,num_col),
                ('Categorical_pipeline',cat_pipeline,cat_col)
            ])
            logging.info("Preprocessor is Returned ")
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transform(self,df_train_path,df_test_path):
        try:
            logging.info("Data Transformation Started ")
            os.makedirs(os.path.dirname(self.transform_config.preprocessor_path),exist_ok=True)
            preprocessor_obj=self.get_tranform_data_object()
            logging.info("Reading train and test data")
            df_train=pd.read_csv(df_train_path)
            df_test=pd.read_csv(df_test_path)

            logging.info("Removing target feature from train and test")
            train_target=df_train['tip']
            df_train=df_train.drop('tip',axis=1)
            test_target=df_test['tip']
            df_test=df_test.drop('tip',axis=1)
            

            logging.info("applying preprocessor on train and test input data features ")
            df_train_transform=preprocessor_obj.fit_transform(df_train)
            df_test_transform=preprocessor_obj.transform(df_test)

## Changes from here
            logging.info("Combining Input and target feature array ")
            df_train_transform=np.c_[df_train_transform,train_target]
            df_test_transform=np.c_[df_test_transform,test_target]
    ## Change completed
            logging.info("Saving our preprocessor to desired path")
            save_object(
                self.transform_config.preprocessor_path,
                preprocessor_obj
            )
            logging.info("Data transformation completed ")
            return(
                df_train_transform,
                df_test_transform
            )
        except Exception as e:
            raise CustomException(e,sys)
