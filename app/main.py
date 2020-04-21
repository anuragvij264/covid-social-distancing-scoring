from flask import Flask, render_template
from flask import request, jsonify
# from config import ALLOWED_EXTENSIONS,UPLOAD_FOLDER,HOST_URL,HOST_NAME
from flask import send_from_directory
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import requests

from api_utils import load_model, gen_img_counts
from config import MODEL_PATH
import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

MODEL = load_model(model_path=MODEL_PATH, device=DEVICE)

app = Flask('__name__')


@app.route('/predict', methods=['GET', 'POST'])
def get_scores():
    content = request.json
    image_path = content['image_path']
    # folder = content['type']
    # image_path = os.path.join(UPLOAD_FOLDER,filepath)
    output = gen_img_counts(image_path, MODEL)
    # final_score = score(output)
    return jsonify({'score': output})


@app.route('/map')
def get_map():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,port = 9999)
