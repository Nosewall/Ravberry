from app import app
from app import watermark
from flask import Flask, render_template, request, redirect, url_for
import os

uploads_dir = os.path.join(app.instance_path, 'uploads')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            filename = os.path.join(uploads_dir, uploaded_file.filename)
            uploaded_file.save(os.path.join(uploads_dir, uploaded_file.filename))
            watermark.watermark_text(filename, uploads_dir, "hello", [50, 50])
        return redirect(url_for('index'))
    return render_template('index.html')