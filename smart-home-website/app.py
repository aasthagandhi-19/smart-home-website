from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'known_faces'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/lights')
def lights():
    return render_template("lights.html")

@app.route('/temperature')
def temperature():
    return render_template("temperature.html")

@app.route('/camera')
def camera():
    return render_template("camera.html")

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['face_image']
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return redirect('/camera')

if __name__ == '__main__':
    app.run(debug=True)

