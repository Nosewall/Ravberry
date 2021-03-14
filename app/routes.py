from app import app
from app import watermark
from pathlib import Path, PureWindowsPath
from flask import Flask, render_template, request, redirect, url_for
import os

uploads_dir = Path(os.path.abspath(os.getcwd()) + "/app/static/uploads")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            filename = os.path.join(str(uploads_dir), uploaded_file.filename)
            uploaded_file.save(os.path.join(uploads_dir, uploaded_file.filename))
            watermark.watermark_text(str(filename), str(uploads_dir), "asdflasdkjfa", [50, 50])
            watermark.watermark_img()
            return render_template('success.html')

=======
from app import app
from app import watermark
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for
import os

uploads_dir = Path(os.path.abspath(os.getcwd()) + "/app/static/uploads")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            filename = os.path.join(str(uploads_dir), uploaded_file.filename)
            uploaded_file.save(os.path.join(uploads_dir, uploaded_file.filename))
            watermark.watermark_text(str(filename), str(uploads_dir), "asdflasdkjfa", [50, 50])
            return render_template('options.html', image_url = "../static/uploads/" + uploaded_file.filename)
    return render_template('index.html')