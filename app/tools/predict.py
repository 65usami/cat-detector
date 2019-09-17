from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import keras, sys
import numpy as np
from PIL import Image
import img_classess


def main(image_file_path):
    classes = img_classess.get_classes()
    image_size = 50
    image = Image.open(image_file_path)
    image = image.convert('RGB')
    image = image.resize((image_size, image_size))
    data = np.asarray(image) / 255
    X = []
    X.append(data)
    X = np.array(X)

    model = load_model('./cat_cnn.h5')
    result = model.predict([X])[0]
    predicted = result.argmax()
    percentage = int(result[predicted] * 100)

    print("======")
    print("{0} ({1} %)".format(classes[predicted], percentage))


if __name__ == "__main__":
    image_file_path = sys.argv[1]
    main(image_file_path)
