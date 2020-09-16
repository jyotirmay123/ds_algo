# from PIL import Image
# import imutils
from flask import Flask, request, Response, send_file, send_from_directory, render_template, url_for, jsonify
# from utils.utills import image_base64, bytes_to_base64
# import numpy as np
# from utils.camera import VideoCamera
import io
# import cv2

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

    return render_template('index.html')


# @app.route('/image', methods=['POST'])
# def image():


if __name__ == '__main__':
    app.run()
