import pandas as pd
import numpy as np
from PIL import Image
import tensorflow as tf

loaded_model = tf.keras.models.load_model("my_cnn_model.h5")

def findLetter(img):
    img = img.convert('L')
    img = img.resize((28, 28))
    input_image = np.array(img)
    input_image = input_image.reshape(1, 28, 28, 1)
    prediction = loaded_model.predict(input_image)
    max_index = np.argmax(prediction)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    predicted_letter = alphabet[max_index]
    return predicted_letter