import os 
import pickle 
import pandas as pd 

from flask import Flask, jsonify, request
import numpy as np

MODEL_PATH = "model/xgb_model.pkl"
with open(MODEL_PATH, "rb") as file:
    xgb = pickle.load(file)
    
# Initilazing the app API
app = Flask(__name__)

# Check app running 
@app.route("/greet", methods=["GET"])
# return messages 
def healthcheck():
    msg = ("Ready to use")
    return jsonify({"message": msg})


# predict function
def predict_function (sample, xgb):
    
    test = pd.DataFrame.from_dict(sample, orient='index')
    
    #drop irelevent features
    drop_columns = ['release_date','duration_ms','valence', 'acousticness','energy','instrumentalness', 'liveness','mode','tempo','key','name','artists','id']         
    
    test.drop(drop_columns,axis=1, inplace=True)
     
    
    #predict
    y_pred = xgb.predict(test)

    return y_pred

# API of predict function
@app.route("/predict", methods=["POST"])
def predict():
    sample = request.get_json()
    predictions = predict_function(sample, xgb)
    
    prediction_str = [str(i) for i in predictions] 
    
    # return results
    result = {
        'prediction': list(prediction_str)
    }
    
    return jsonify(result)


# evaluate function
def evaluate_function(sample, xgb):
    
    test = pd.DataFrame.from_dict(sample, orient='index')
    
    #drop irelevent features
    drop_columns = ['release_date','duration_ms','valence', 'acousticness','energy','instrumentalness', 'liveness','mode','tempo','key','name','artists','id']  
    
    test.drop(drop_columns,axis=1, inplace=True)

    # data transformation
    median = test['popularity'].median()
    test.loc[test['popularity'] < median, 'popularity'] = 0
    test.loc[test['popularity'] >= median, 'popularity'] = 1


    X_test = test.drop(['popularity'],axis=1)
    y_test = test['popularity']
    
    #predict
    y_pred = xgb.predict(X_test)
    
    # evaluate 
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy



# API of evaluate function 
@app.route("/evaluate", methods=["POST"])
def evaluate():
    sample = request.get_json()
    accuracy = evaluate_function(sample, xgb)
    
    result = {
        'accuracy': accuracy
    }
    
    return jsonify(result)
    
# main 
if __name__ == '__main__': 
    app.run(debug=True)


