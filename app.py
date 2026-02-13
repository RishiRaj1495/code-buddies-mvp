from flask import Flask, render_template, request
import numpy as np
import joblib
import tensorflow as tf

app = Flask(__name__)
model = tf.keras.models.load_model('diabetes_model.h5')
scaler = joblib.load('scaler.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    risk = None
    if request.method == 'POST':
        features = [
            float(request.form['preg']),
            float(request.form['glucose']), 
            float(request.form['pressure']),
            float(request.form['thickness']),
            float(request.form['insulin']),
            float(request.form['bmi']),
            float(request.form['pedigree']),
            float(request.form['age'])
        ]
        data = scaler.transform([features])
        risk = model.predict(data, verbose=0)[0][0]
    
    return render_template('index.html', risk=risk)

if __name__ == '__main__':
    app.run(debug=True)
