from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection
import img_classess

classes_header = "imgs"
classes = img_classess.get_classes()
num_classes = len(classes)
image_size = 50


def generate_train_data():
    X = []
    Y = []
    for index, classlabel in enumerate(classes):
        print(index, classlabel)
        photos_dir = "./" + classes_header + '/' + classlabel
        files = glob.glob(photos_dir + "/*.jpg")
        for i, file in enumerate(files):
            image = Image.open(file)
            image = image.convert("RGB")
            image = image.resize((image_size, image_size))
            data = np.asarray(image)
            X.append(data)
            Y.append(index)
    X = np.array(X)
    Y = np.array(Y)
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
    xy = (X_train, X_test, y_train, y_test)
    np.save("./train.npy", xy)


if __name__ == "__main__":
    generate_train_data()
