from joblib import load
import json
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

from train import load_images, load_labels, preprocess


def main(repo_path):
    test_csv_path = repo_path / "data/prepared/test.csv"
    test_df = pd.read_csv(test_csv_path)
    raw_images = load_images(data_frame=test_df, column_name="filename")
    labels = load_labels(data_frame=test_df, column_name="label")
    preprocessed = [preprocess(image) for image in raw_images]
    test_data = np.concatenate(preprocessed, axis=0)
    model_path = repo_path / "model"
    model = load(model_path / "model.joblib")
    predictions = model.predict(test_data)
    accuracy = accuracy_score(labels, predictions)
    metrics = {"accuracy": accuracy}
    accuracy_path = repo_path / "metrics/accuracy.json"
    accuracy_path.write_text(json.dumps(metrics))


if __name__ == "__main__":
    repo_path = Path(__file__) / "../.."
    main(repo_path.resolve())
