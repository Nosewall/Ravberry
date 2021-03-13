from app import app
from app import watermark
from flask import Flask, render_template, request, redirect, url_for
import os

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)

        return redirect(url_for('index'))
    return render_template('index.html')