import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import apps.predict as predict
import apps.file_checker as file_checker

app = Flask(__name__)
app.secret_key = 'secret_key'
STATIC_PUSHED_DATA_PATH = '/static/pushed_data'
UPLOAD_FOLDER = app.root_path + STATIC_PUSHED_DATA_PATH
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

        if file and file_checker.is_allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            result_data = predict.cat(
                file_path, app.root_path + '/apps/cat_cnn.h5')
            pushed_img_path = STATIC_PUSHED_DATA_PATH + '/' + filename
            return redirect(url_for('upload_file', filename=filename, result_data=result_data, pushed_img_path=pushed_img_path))

    result_data = request.args.get('result_data')
    filename = request.args.get('filename')
    pushed_img_path = request.args.get('pushed_img_path')
    return render_template('upload_file.html', title='upload_file', filename=filename, result_data=result_data, pushed_img_path=pushed_img_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
