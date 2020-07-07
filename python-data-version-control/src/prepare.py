from pathlib import Path
import pandas as pd

folders_to_labels = {"n03445777": "golf ball", "n03888257": "parachute"}


def get_filelist_and_labels(source_path, target_folders):
    images = []
    labels = []
    for image_path in source_path.rglob("*/*.JPEG"):
        filename = image_path.absolute()
        folder = image_path.parts[-2]
        if folder in target_folders:
            images.append(filename)
            label = folders_to_labels[folder]
            labels.append(label)
    return images, labels


def save_as_csv(filenames, labels, destination):
    data_dictionary = {"filename": filenames, "label": labels}
    data_frame = pd.DataFrame(data_dictionary)
    data_frame.to_csv(destination)


def main(repo_path):
    data_path = repo_path / "data"
    train_path = data_path / "raw/train"
    test_path = data_path / "raw/val"
    train_filenames, train_labels = get_filelist_and_labels(
        train_path, folders_to_labels.keys()
    )
    test_filenames, test_labels = get_filelist_and_labels(
        test_path, folders_to_labels.keys()
    )
    prepared = data_path / "prepared"
    save_as_csv(train_filenames, train_labels, prepared / "train.csv")
    save_as_csv(test_filenames, test_labels, prepared / "test.csv")


if __name__ == "__main__":
    repo_path = Path(__file__) / "../.."
    main(repo_path.resolve())
