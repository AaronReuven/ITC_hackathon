import pickle

import flask
import os
from model_creation_code.config import *
import pandas as pd
from flask import Flask
import json

app = Flask(__name__)


@app.route('/predict_drawing', methods=['POST'])
def predict_bulk():
    """
    runs the predictions on the model of dataframe passed as json
    :return: json of predictions
    """
    if 'model' not in globals():
        model = read_model(MODEL_FILE)
    predict_data = json.loads(flask.request.get_json())
    predict_df = pd.DataFrame(predict_data)
    results = model.predict(predict_df)
    result = {RESULT_JSON_TAG: results.tolist()}
    return flask.jsonify(result)


# @app.route('/predict_drawing')
# def predict():
#     """
#     predicts a single sample from the parameters of the calling route
#     :return: string of prediction
#     """
#     if 'model' not in globals():
#         model = read_model(MODEL_FILE)
#     return str(
#         model.predict(np.array([float(num) for num in request.args.values()]).astype(dtype=float).reshape(1, -1))[0])


def read_model(file):
    """
    reads the model from file
    :param file: file to read the model from
    :return: trained model from file
    """
    model = None
    with open(file, 'rb') as f:
        model = pickle.load(f)
    return model


def main():
    model = read_model(MODEL_FILE)
    return model


if __name__ == '__main__':
    model = main()
    port = os.environ.get('PORT')
    if port:
        # 'PORT' variable exists - running on Heroku, listen on external IP and on given by Heroku port
        app.run(host='0.0.0.0', port=int(port))
    else:
        # 'PORT' variable doesn't exist, running not on Heroku, presumabely running locally, run with default
        #   values for Flask (listening only on localhost on default Flask port)
        app.run()
