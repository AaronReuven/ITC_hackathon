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
URL_BULK = 'https://itc-exercise.herokuapp.com/predict_churn_bulk'
