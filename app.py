from flask import Flask
from flask import request
app = Flask(__name__)

from volume import get_amplitdue

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

@app.route("/getvolume", methods=['POST'])
def get_volume():
    file = request.files['audio_file']
    avgDeci = get_amplitdue(file)
    return avgDeci