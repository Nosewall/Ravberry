from app import app
from app import watermark
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for
import os

uploads_dir = Path(os.path.abspath(os.getcwd()) + "/app/static/uploads")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            filename = os.path.join(str(uploads_dir), uploaded_file.filename)
            uploaded_file.save(os.path.join(uploads_dir, uploaded_file.filename))
            return render_template(
                "options.html", image_url="../static/uploads/" + uploaded_file.filename
            )
    return render_template("index.html")


@app.route("/options", methods=["GET", "POST"])
def options():
    if request.method == "POST":
        # water_mark = request.files["watermark"]
        # text = request.form["text"]
        # resolution = request.form["resolution"]
        # font = request.form["fonts"]
        if uploaded_file.filename[-3:] == "png" or uploaded_file.filename[-3:] == "gif":
            print("transparency")
            watermark.watermark_with_transparency(
                str(filename), str(uploads_dir), " ", [50, 50]
            )
            return render_template(
                "options.html", image_url="../static/uploads/" + uploaded_file.filename
            )
        else:
            print("solid")
            watermark.watermark_img(str(filename), str(uploads_dir), text, [50, 50])