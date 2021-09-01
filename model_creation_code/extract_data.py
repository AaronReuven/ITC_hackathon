import pandas as pd
import numpy as np
from google.cloud import storage
from configurations.config import *
import os


def get_data(list_of_classes):
    for cls in list_of_classes:
        if os.path.exists(cls + FILE_EXT):
            continue
        storage_client = storage.Client.create_anonymous_client()
        bucket = storage_client.bucket(BUCKET)
        blob = bucket.blob(OBJECT_PATH + cls + FILE_EXT)
        blob.download_to_filename(DATA_PATH + cls + FILE_EXT)


def mush_into_dataframe(list_of_classes):
    dfs = []
    for cls in list_of_classes:
        array = np.load(DATA_PATH + cls + FILE_EXT)
        df = pd.DataFrame(array)
        df['label'] = np.full((array.shape[0], 1), cls)
        dfs.append(df)
    return pd.concat(dfs)


