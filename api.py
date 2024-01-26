from flask import Flask, request
from tensorflow import keras
import numpy as np


app = Flask(__name__)

model = keras.models.load_model('mnistModel.h5')

@app.route('/classify',methods=['POST'])
def test_model():
    data = request.get_json(force=True)

    data = reformating(data["file"])

    prediction = model.predict(data)
    val = int(np.argmax(prediction))

    return {"prediction":val}

def formating_data(a):
    return a.reshape(-1,28,28,1)

def reformating(text):
    
    a = text.split(',')
    a = [int(elem)/255 for elem in a]
    a = np.array(a)

    a = a.reshape(-1,28,28,1)

    return a


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)