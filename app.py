from flask import Flask
from flask import request
from flask_cors import CORS
from flask import Response
app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

from volume import get_amplitdue

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

@app.route("/getvolume", methods=['POST'])
def get_volume():
    # avgDeci = get_amplitdue(file)
    # return avgDeci
    data = request.make_form_data_parser()
    data = data.parse(request.files.get('audio_file'))
    return(data)