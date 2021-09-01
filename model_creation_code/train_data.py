import pickle
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from model_creation_code.extract_data import get_data, mush_into_dataframe
from configurations.config import *


def read_data():
    get_data(CLASSES)
    return mush_into_dataframe(CLASSES)


def split_data(data):
    X = data.drop(columns='label')
    y = data['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=TRAIN_SIZE, random_state=RANDOM_STATE)
    return X_train, X_test, y_train, y_test


def preprocess(X_train, X_test, y_train, y_test):
    lbl_encoder = LabelEncoder()
    y_train = lbl_encoder.fit_transform(y_train)
    y_test = lbl_encoder.transform(y_test)
    return X_train, X_test, y_train, y_test


def train_model(x, y):
    clf = BernoulliNB(binarize=0)
    clf.fit(x, y)
    return clf


def save_model(model, target_file):
    """
    pickle the model and save it to a pickle file
    :param model: model to pickle
    :param target_file: to which file to save it to
    :return:
    """
    with open(target_file, 'wb') as f:
        pickle.dump(model, f)


def print_results(predicted_target, true_target):
    print(classification_report(true_target, predicted_target))


def main():
    data = read_data()
    X_train, X_test, y_train, y_test = split_data(data)
    X_train, X_test, y_train, y_test = preprocess(X_train, X_test, y_train, y_test)
    model = train_model(X_train, y_train)
    print_results(model.predict(X_test), y_test)
    save_model(model, MODEL_FILE)


if __name__ == '__main__':
    main()
