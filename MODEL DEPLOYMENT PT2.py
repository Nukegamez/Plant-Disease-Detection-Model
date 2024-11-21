import numpy
import cv2
import os
import tensorflow
from flask import Flask, request, flash, redirect, send_file
from tensorflow.keras import datasets, layers, models

app = Flask(__name__)



model = tensorflow.keras.models.load_model('#insert the path to .keras model', compile=False)

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']

    if file:
        filename = file.filename
        filename = os.path.join('C:/', filename)
        file.save(filename)

        score = tensorflow.nn.softmax(model.predict(tensorflow.expand_dims(tensorflow.keras.utils.img_to_array(cv2.imread(filename)/255.0), 0)
)[0])

        result = "This image most likely belongs to "+str(class_names[numpy.argmax(score)])+" with a "+str(100 * numpy.max(score))+" percent confidence."

    return result

if __name__ == '__main__':
    app.run(debug=True)

