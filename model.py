from flask import Flask, jsonify
import pandas as pd
import json
import pickle
from xgboost import XGBClassifier
import numpy as np


app = Flask(__name__)


@app.route('/predict')
def predict():
     query= pd.read_json('validation.json')
     classifier = pickle.load(open('xgb.pkl', 'rb'))
     prediction = classifier.predict(query)
     list_predict = prediction.tolist()

     return jsonify({'prediction': list_predict})
     


if __name__ == '__main__':
     app.run(port=8080, debug=True)