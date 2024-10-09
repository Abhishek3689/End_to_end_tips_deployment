import os
import sys  
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransform
from src.components.model_trainer import ModelTrainer
from dataclasses import dataclass

@dataclass
class DataingestionConfig:
    train_data_path=os.path.join("Source","train.csv")
    test_data_path=os.path.join("Source","test.csv")
    raw_data_path=os.path.join("Source","raw.csv")


class Dataingestion(DataingestionConfig):
    def __init__(self):
        self.ingestion_config=DataingestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started ")
        try:

            df=pd.read_csv('data/tips.csv')
            logging.info("Read data as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            logging.info("Store the raw data in our required folder")
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("splitting the data in train and test")
            df_train,df_test=train_test_split(df,test_size=.25,random_state=34)

            logging.info("storing train and test data for further processing")
            df_train.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            df_test.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Data Ingestion Completed and returning train and test path for data transforation process")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=Dataingestion()
    train_data_path1,test_data_path1=obj.initiate_data_ingestion()

    transform_obj=DataTransform()
    train_array,test_array=transform_obj.initiate_data_transform(train_data_path1,test_data_path1)

    model_obj=ModelTrainer()
    model_obj.initiate_model_training(train_array,test_array)
  
    print(train_array.shape)
    
    #print(test_array[:5])