import pandas as pd
import os,sys
from flask import Flask,render_template,request
from src.pipeline.prediction_pipeline import CustomData,Prediction_Pipeline
pred_pipe=Prediction_Pipeline()
from src.logger import logging
from src.exception import CustomException
app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/submit_form',methods=['POST'])
def predict_tip():
        try:
        # if request.method=='GET':
        #     return render_template('home.html')
        # else:
            logging.info("collecting data from form ")
            data=CustomData(
            total_bill = request.form.get('total_bill'),
            size = request.form.get('size'),
            sex = request.form.get('sex'),
            smoker = request.form.get('smoker'),
            day = request.form.get('day'),
            time = request.form.get('time'))
            
            df_pred=data.get_custom_data_as_frame()
            logging.info("Created Dataframe from input form")
            res=pred_pipe.predict(df_pred)
            
            logging.info("Result has been renderd to index template")
            return render_template('index.html',result=round(res[0],2))
        except Exception as e:
             raise CustomException(e,sys)
        
        
if __name__=="__main__":

    app.run(host="0.0.0.0",port=80)