import pathlib
import pickle
from collections import defaultdict

from PIL import Image, ImageDraw

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


def recognize_faces(
    image_location: str,
    model: str = "hog",
    encodings_location: str = DEFAULT_ENCODINGS_PATH,
) -> None:
    with open(encodings_location, "rb") as f:
        loaded_encodings = pickle.load(f)

    input_image = face_recognition.load_image_file(image_location)

    input_face_locations = face_recognition.face_locations(
        input_image, model=model
    )
    input_face_encodings = face_recognition.face_encodings(
        input_image, input_face_locations
    )

    pillow_image = Image.fromarray(input_image)
    draw = ImageDraw.Draw(pillow_image)

    for (top, right, bottom, left), unknown_encoding in zip(
        input_face_locations, input_face_encodings
    ):
        boolean_matches = face_recognition.compare_faces(
            loaded_encodings["encodings"], unknown_encoding
        )
        result = "Not found"

        match_indexes = []
        name_frequency = defaultdict(int)
        for index, match in enumerate(boolean_matches):
            if match:
                match_indexes.append(index)

        for index in match_indexes:
            name = loaded_encodings["names"][index]
            name_frequency[name] += 1

        if name_frequency:
            result = max(name_frequency, key=lambda key: name_frequency[key])

        draw.rectangle(((left, top), (right, bottom)), outline=(51, 51, 255))
        _, caption_height = draw.textsize(result)
        draw.rectangle(
            ((left, bottom - caption_height - 10), (right, bottom)),
            fill=(51, 51, 255),
            outline=(51, 51, 255),
        )
        draw.text(
            (left + 6, bottom - caption_height - 5),
            result,
            fill=(255, 255, 255, 255),
        )

    del draw
    pillow_image.show()

recognize_faces("two-presidents.webp")
