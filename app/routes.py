from app import app
from app import watermark
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for
import os

uploads_dir = Path(os.path.abspath(os.getcwd()) + "/app/static/uploads")
watermarks_dir = Path(os.path.abspath(os.getcwd()) + "/app/static/watermarks/WatermarkTemplate.png")

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            filename = os.path.join(str(uploads_dir), uploaded_file.filename)
            uploaded_file.save(os.path.join(uploads_dir, uploaded_file.filename)) 
            uploaded_fileasdf = uploaded_file.filename
            print(uploaded_fileasdf)
            return redirect(url_for('options', uploaded_file=uploaded_file.filename))
    return render_template("index.html")

@app.route("/options/<uploaded_file>", methods=["GET", "POST"])
def options(uploaded_file):
    if request.method == "POST":
        print(request.form["position"])

        # text = request.form["text"]
        # resolution = request.form["resolution"]
        # font = request.form["fonts"]
        if uploaded_file[-3:] == "png" or uploaded_file[-3:] == "gif":
            print("transparency")
            image_path = str(uploads_dir) + "\\" + uploaded_file
            watermark.watermark_with_transparency(
                image_path, str(uploads_dir), watermarks_dir, [50, 50], int(request.form["resolution"])
            )
            return render_template(
                "options.html", image_url="../static/uploads/" + uploaded_file
            )
        else:
            print("solid")
            watermark.watermark_img(str(filename), str(uploads_dir), text, [50, 50])
    else:
        return render_template("options.html", image_url="../static/uploads/" + uploaded_file)