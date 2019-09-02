import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as keras_backend
import keras,sys
import numpy as np
from PIL import Image
import tools.img_classess as img_classess



def predict(file):

    classes = img_classess.get_classes()

    image_size = 50
    image = Image.open(file)
    image = image.convert('RGB')
    image = image.resize((image_size, image_size))
    data = np.asarray(image)/255
    X = []
    X.append(data)
    X = np.array(X)

    model = load_model('./tools/cat_cnn.h5')
    result = model.predict([X])[0]

    keras_backend.clear_session()

    predicted = result.argmax()
    percentage = int(result[predicted] * 100)

    result_data = classes[predicted] + ' (' + str(percentage) + '%)'
    return result_data

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'secret_key'
STATIC_PUSHED_DATA_PATH = '/static/pushed_data'
UPLOAD_FOLDER = app.root_path + STATIC_PUSHED_DATA_PATH
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/ht')
def hello():
    return render_template('hello.html', title='flask test')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            print(file_path)

            result_data = predict(file_path)
            pushed_img_path = STATIC_PUSHED_DATA_PATH + '/' + filename

            return redirect(url_for('upload_file', filename=filename, result_data=result_data, pushed_img_path=pushed_img_path))

    result_data = request.args.get('result_data')
    filename = request.args.get('filename')
    pushed_img_path = request.args.get('pushed_img_path')
    return render_template('upload_file.html', title='upload_file', filename=filename, result_data=result_data, pushed_img_path=pushed_img_path)
