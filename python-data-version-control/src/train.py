from joblib import dump
from pathlib import Path
import numpy as np
import pandas as pd
from skimage.io import imread_collection
from skimage.transform import resize
from sklearn.linear_model import SGDClassifier


def load_images(data_frame, column_name):
    filelist = data_frame[column_name].to_list()
    image_list = imread_collection(filelist)
    return image_list


def load_labels(data_frame, column_name):
    label_list = data_frame[column_name].to_list()
    return label_list


def preprocess(image):
    resized = resize(image, (100, 100, 3))
    reshaped = resized.reshape((1, 30000))
    return reshaped


def main(repo_path):
    train_csv_path = repo_path / "data/prepared/train.csv"
    train_df = pd.read_csv(train_csv_path)
    raw_images = load_images(data_frame=train_df, column_name="filename")
    labels = load_labels(data_frame=train_df, column_name="label")
    preprocessed = [preprocess(image) for image in raw_images]
    train_data = np.concatenate(preprocessed, axis=0)
    sgd = SGDClassifier(max_iter=10)
    trained_model = sgd.fit(train_data, labels)
    model_path = repo_path / "model"
    dump(trained_model, model_path / "model.joblib")


if __name__ == "__main__":
    repo_path = Path(__file__) / "../.."
    main(repo_path.resolve())
