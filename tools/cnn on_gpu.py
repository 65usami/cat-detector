from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import tensorflow as tf
import keras
import numpy as np
import img_classess

from keras.backend import tensorflow_backend
config = tf.ConfigProto(gpu_options=tf.GPUOptions(allow_growth=True))
session = tf.Session(config=config)
tensorflow_backend.set_session(session)

classes = img_classess.get_classes()
num_classes = len(classes)

def main():
    X_train, X_test, y_train, y_test = np.load("./animal.npy", allow_pickle=True)
    X_train = X_train.astype("float") / 255
    X_test = X_test.astype("float") / 255
    y_train = np_utils.to_categorical(y_train, num_classes)
    y_test = np_utils.to_categorical(y_test, num_classes)

    model = model_train(X_train, y_train)
    model_eval(model, X_test, y_test)

def model_train(X, y):
    model = Sequential()
    model.add(
        Conv2D(
            32,
            (3,3),
            activation='relu',
            padding='same',
            input_shape=(X[0].shape),
            kernel_initializer=keras.initializers.TruncatedNormal(stddev=0.1),
            bias_initializer=keras.initializers.constant(0.1)
        )
    )

    model.add(MaxPooling2D(pool_size=(3, 3)))
    model.add(Dropout(rate=0.2))

    model.add(
        Conv2D(
            64,
            kernel_size=(3, 3),
            activation='relu',
            padding='same'
        )
    )

    model.add(Dropout(rate=0.2))

    model.add(
        Conv2D(
            128,
            kernel_size=(3, 3),
            activation='relu'
        )
    )

    model.add(MaxPooling2D(pool_size=(3, 3)))
    model.add(Dropout(rate=0.2))

    model.add(Flatten())
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))

    opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)
    model.compile(loss='categorical_crossentropy',optimizer=opt,metrics=['accuracy'])

    model.fit(
        X,
        y,
        batch_size=80,
        epochs=3000,
        verbose=True,
        callbacks=[
            keras.callbacks.EarlyStopping(
            monitor='loss',
            min_delta=0,
            patience=100,
            verbose=1
            )
        ]
    )

    model.save('./cat_cnn.h5')

    return model

def model_eval(model, X, y):
    scores = model.evaluate(X, y, verbose=1)
    print('Test Loss: ', scores[0])
    print('Test Accuracy: ', scores[1])

if __name__ == "__main__":
    main()