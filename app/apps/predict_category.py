from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import keras, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random, string


def __randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

def __save_png_from_text(text, file_path, fontpath):
    img = Image.new('RGB', (600, 45), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(fontpath, 15)
    d.text((5, 10), str(text), fill=(0,0,0), font=font)
    img.save(file_path)

def category(text_value, app_path):
    model = load_model(app_path + '/apps/category_cnn.h5')

    file_path = '/tmp/' + __randomname(40) + '.png'

    fontpath = app_path + '/apps/GenShinGothic-Normal.ttf'

    __save_png_from_text(text_value, file_path, fontpath)
    image = Image.open(file_path)

    image = image.convert('RGB')
    data = np.asarray(image) / 255
    X = []
    X.append(data)
    X = np.array(X)
    result = model.predict([X])[0]

    predicted = result.argmax()

    name = None
    if predicted == 0:
        name = '会社'
    elif predicted == 1:
        name = '住所'
    elif predicted == 2:
        name = '郵便番号'
    elif predicted == 3:
        name = '電話番号'
    elif predicted == 4:
        name = 'URL'

    result_value = str(text_value) + " = " + str(name)
    print(result_value)

    return result_value
