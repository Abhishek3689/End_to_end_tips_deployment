from src.logger import logging
import os
import pickle
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error


def save_object(file_path,file_obj):
    logging.info("file saving started ")
    with open(file_path,'wb') as f_obj:
        pickle.dump(file_obj,f_obj)

def evaluate_model(X_train,X_test,y_train,y_test,models):
    reports={}
    for i in range(len(models)):
        model=list(models.values())[i]
        model.fit(X_train,y_train)
        y_pred=model.predict(X_test)
        score=r2_score(y_test,y_pred)
        reports[list(models.keys())[i]]=score
    return reports

def load_object(file_path):
    with open(file_path,'rb') as f_obj:
        return pickle.load(f_obj)