import pandas as pd

# google storage
BUCKET = 'quickdraw_dataset'
OBJECT_PATH = 'full/numpy_bitmap/'
FILE_EXT = '.npy'
CLASSES = ['ant', 'penguin', 'horse', 'zebra']
DATA_PATH = 'fetched_data/'

# model params
TRAIN_SIZE = 0.75
RANDOM_STATE = 26
MODEL_FILE = 'model/draw_model.pkl'


# REST API
RESULT_JSON_TAG = 'result'
URL_BULK = 'https://itc-hackathon.herokuapp.com/predict_drawing'
URL_TEST = 'https://ec2-3-70-29-25.eu-central-1.compute.amazonaws.com/predict_drawing/'

# S3 bucket
S3_MODEL_FILE = 'draw_model.pkl'
DRAW_BUCKET = 'drawmodel'
s3_cred_df = pd.read_csv('/home/roni/PycharmProjects/ITC_hackathon/configurations/rootkey.csv')
ACCESS_ID = s3_cred_df['AWSAccessKeyId'][0]
ACCESS_KEY = s3_cred_df['AWSSecretKey'][0]
DOWNLOAD_MODEL_PATH = 'model'
