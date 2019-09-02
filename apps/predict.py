from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as keras_backend
import keras,sys
import numpy as np
from PIL import Image

def cat(img_file, h5_file):
    classes = ["cat", "monkey", "bird", "dog"]
    model = load_model(h5_file)

    image = Image.open(img_file)
    image = image.convert('RGB')
    image_size = 50
    image = image.resize((image_size, image_size))
    data = np.asarray(image)/255
    X = []
    X.append(data)
    X = np.array(X)

    result = model.predict([X])[0]
    keras_backend.clear_session()
    predicted = result.argmax()
    percentage = int(result[predicted] * 100)
    result_data = classes[predicted] + ' (' + str(percentage) + '%)'
    return result_data