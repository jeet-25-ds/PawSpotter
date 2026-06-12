from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

#model = load_model("../models/dog_cat_model.h5")

import os
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "dog_cat_model.h5"
)

model = load_model(MODEL_PATH)


def predict_image(image_path):

    img = image.load_img(
        image_path,
        target_size=(96,96)
    )

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)

    img_array = img_array / 255.0

    prediction = model.predict(img_array)

    confidence = float(prediction[0][0])

    if confidence > 0.5:
        label = "Dog"
        confidence_percent = confidence * 100
    else:
        label = "Cat"
        confidence_percent = (1 - confidence) * 100

    return label, confidence_percent

if __name__ == "__main__":

    image_path = os.path.join(
        BASE_DIR,
        "test_images",
        "dog1.jpg"
    )

    label, confidence = predict_image(image_path)

    print(f"Prediction: {label}")
    print(f"Confidence: {confidence:.2f}%")