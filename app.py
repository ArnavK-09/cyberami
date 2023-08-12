# imports 
from flask import Flask, request, render_template
import pickle
import numpy as np

# init
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def hello_world():
    """
        GET /
    """
    return render_template("main.html")


@app.route('/predict', methods=['POST'])
def predict():
    """
        POST /predict
    """
    inputs = [(x) for x in request.form.values()]
    prediction = model.predict([inputs[0]])[0]
    result = "Safe" if prediction == 1 else "Harmful"
    return render_template('main.html', res=result)
