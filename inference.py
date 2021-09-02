import base64
import pickle
import flask
import os
# from boto3.session import Session
import boto3
import numpy as np

from configurations.config import *
import pandas as pd
from flask import Flask
from flask_cors import CORS, cross_origin
import json
from PIL import Image
import skimage
from io import BytesIO

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def read_new_image(image_file_name):
    image = skimage.io.imread(image_file_name)
    return image


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


model = read_model(os.path.abspath(MODEL_FILE))


@app.route('/predict_drawing', methods=['POST'])
@cross_origin()
def predict_bulk():
    """
    runs the predictions on the model of dataframe passed as json
    :return: json of predictions
    """
    r = flask.request.args.get('b_str')
    # print(r)
    # predict_data = json.loads(r)
    # print(predict_data)
    # b_srt = r[22:]
    base64_img_bytes = r.encode('utf-8')
    # with open('decoded_image.png', 'wb') as file_to_save:
    decoded_image_data = base64.decodebytes(base64_img_bytes)
        # file_to_save.write(decoded_image_data)
    # Image.open(BytesIO(decoded_image_data))
    img = Image.open(BytesIO(decoded_image_data)).convert('1').resize((28, 28))
    img.save('x_pred.jpg')

    x_pred = read_new_image('x_pred.jpg')
    predict_df = pd.DataFrame(np.array([x_pred]))

    # r = flask.request.data
    # nparr = np.fromstring(r,np.uint8)
    # predict_df = pd.DataFrame(nparr)
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
