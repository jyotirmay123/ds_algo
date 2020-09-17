# from PIL import Image
# import imutils
from flask import Flask, request, Response, send_file, send_from_directory, render_template, url_for, jsonify
# from utils.utills import image_base64, bytes_to_base64
# import numpy as np
# from utils.camera import VideoCamera
import io
# import cv2
import os
import json
app = Flask(__name__)

# vc = VideoCamera()


# for CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')  # Put any other methods you need here
    return response


@app.route('/')
def hello_world():
    data = dict()
    data['ds_algo'] = os.listdir('static/practise/ds_algo/')
    ds_content = {}
    for algo in data['ds_algo']:
        ds_content[algo] = {}
        for file in os.listdir(f'static/practise/ds_algo/{algo}/'):
            if file.split('.')[-1] is not 'png':
                with open(f'static/practise/ds_algo/{algo}/{file}', encoding="utf8", errors='ignore') as f:
                    txt = f.read()
                    ds_content[algo][file] = txt
            else:
                ds_content[algo][file] = 'AN IMAGE FILE.'

    data['german'] = os.listdir('static/practise/german/')
    german_content = {}
    for lessons in data['german']:
        german_content[lessons] = {}
        for file in os.listdir(f'static/practise/german/{lessons}/'):
            if file.split('.')[-1] == 'json':
                with open(f'static/practise/german/{lessons}/{file}', encoding="utf8", errors='ignore') as f:
                    txt = f.read()
                    german_content[lessons] = json.loads(txt)

    data['diet_gym'] = os.listdir('static/practise/diet_gym/')
    gym_content = {}
    for workout in data['diet_gym']:
        gym_content[workout] = {}
        for file in os.listdir(f'static/practise/diet_gym/{workout}/'):

            gym_content[workout][file.split('.')[0]] = f'static/practise/diet_gym/{workout}/{file}'

    gym_content_keys = {}
    for workout in data['diet_gym']:
        gym_content_keys[workout] = list(gym_content[workout].keys())

    print(gym_content)
    return render_template('index.html',
                           datas=data,
                           keys=list(data.keys()),
                           ds_content=ds_content,
                           german_content=german_content,
                           gym_content=gym_content,
                           gym_content_keys=gym_content_keys)


# @app.route('/image', methods=['POST'])
# def image():


if __name__ == '__main__':
    app.run()
