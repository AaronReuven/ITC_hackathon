import pickle
import flask
import os
# from boto3.session import Session
import boto3
from configurations.config import *
import pandas as pd
from flask import Flask
import json

app = Flask(__name__)


def read_model(file):
    """
    reads the model from file
    :param file: file to read the model from
    :return: trained model from file
    """
    # print('Downloading model')
    # if not os.path.exists(DOWNLOAD_MODEL_PATH):
    #     os.mkdir(DOWNLOAD_MODEL_PATH)
    # s3 = boto3.resource('s3', aws_access_key_id=ACCESS_ID, aws_secret_access_key=ACCESS_KEY)
    # s3.meta.client.download_file(DRAW_BUCKET, S3_MODEL_FILE, os.path.abspath(DOWNLOAD_MODEL_PATH) + '/' + S3_MODEL_FILE)
    # print('finished downloading')
    model = None
    # with open(os.path.abspath(DOWNLOAD_MODEL_PATH) + '/' + S3_MODEL_FILE, 'rb') as f:
    with open(file, 'rb') as f:
        model = pickle.load(f)
    return model


model = read_model(os.path.abspath(MODEL_FILE))


@app.route('/predict_drawing', methods=['POST'])
def predict_bulk():
    """
    runs the predictions on the model of dataframe passed as json
    :return: json of predictions
    """
    # if 'model' not in globals():
    #     model = read_model(os.path.abspath(MODEL_FILE))
    predict_data = json.loads(flask.request.get_json())
    # return predict_data
    # return 'can load'
    predict_df = pd.DataFrame(predict_data)
    results = model.predict_proba(predict_df)
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
@app.route('/hi')
def hi():
    return 'hi'


# def main():
#     model = read_model(os.path.abspath(MODEL_FILE))
#     return model
    # pass


if __name__ == '__main__':
    # model = main()
    port = os.environ.get('PORT')
    if port:
        # 'PORT' variable exists - running on Heroku, listen on external IP and on given by Heroku port
        app.run(host='0.0.0.0', port=int(port))
    else:
        # 'PORT' variable doesn't exist, running not on Heroku, presumabely running locally, run with default
        #   values for Flask (listening only on localhost on default Flask port)
        app.run()
