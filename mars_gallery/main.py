import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'mars_gallery_secret_key'

UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
MAX_FILE_SIZE = 16 * 1024 * 1024

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_gallery_images():
    images = []
    if os.path.exists(UPLOAD_FOLDER):
        for filename in os.listdir(UPLOAD_FOLDER):
            if allowed_file(filename) and not filename.startswith('.'):
                images.append(filename)
    return sorted(images)


@app.route('/')
def index():
    images = get_gallery_images()
    return render_template('gallery.html', images=images)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Файл не найден в запросе', 'danger')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('Файл не выбран', 'warning')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            if os.path.exists(filepath):
                flash(f'Файл {filename} уже существует!', 'warning')
                return redirect(request.url)

            try:
                file.save(filepath)
                flash(f'Изображение {filename} успешно загружено!', 'success')
                return redirect(url_for('index'))
            except Exception as e:
                flash(f'Ошибка при сохранении: {str(e)}', 'danger')
                return redirect(request.url)
        else:
            flash('Недопустимый формат файла. Разрешены: PNG, JPG, JPEG, GIF, WEBP', 'danger')
            return redirect(request.url)

    return render_template('upload.html')


@app.route('/delete/<filename>', methods=['POST'])
def delete_image(filename):
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
        if os.path.exists(filepath):
            os.remove(filepath)
            flash(f'Изображение {filename} удалено', 'info')
        else:
            flash('Файл не найден', 'warning')
    except Exception as e:
        flash(f'Ошибка при удалении: {str(e)}', 'danger')

    return redirect(url_for('index'))


@app.errorhandler(413)
def file_too_large(e):
    flash(f'Файл слишком большой! Максимальный размер: {MAX_FILE_SIZE // 1024 // 1024} MB', 'danger')
    return redirect(url_for('upload'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
