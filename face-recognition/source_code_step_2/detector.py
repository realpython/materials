import pathlib
import pickle

import face_recognition

DEFAULT_ENCODINGS_PATH = "output/encodings.pkl"


def encode_known_faces(
    model: str = "hog", encodings_location: str = DEFAULT_ENCODINGS_PATH
) -> None:
    names = []
    encodings = []
    for filepath in pathlib.Path("training").glob("*/*"):
        name = filepath.parent.name
        image = face_recognition.load_image_file(filepath)

        face_locations = face_recognition.face_locations(image, model=model)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        for encoding in face_encodings:
            names.append(name)
            encodings.append(encoding)

    name_encodings = {"names": names, "encodings": encodings}
    with open(encodings_location, "wb") as f:
        pickle.dump(name_encodings, f)


encode_known_faces()
