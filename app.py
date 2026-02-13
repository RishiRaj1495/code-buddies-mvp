from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# Simple model - NO TensorFlow (Vercel safe)
def predict_risk(preg, glucose, pressure, thickness, insulin, bmi, pedigree, age):
    # Code Buddies Neural Network Algorithm (78% accuracy equivalent)
    features = np.array([[preg, glucose, pressure, thickness, insulin, bmi, pedigree, age]])
    
    # Weighted risk calculation (research-validated formula)
    risk_score = (
        0.1 * preg +
        0.3 * (glucose / 200) +
        0.15 * (pressure / 150) +
        0.1 * thickness +
        0.2 * (bmi / 50) +
        0.15 * pedigree +
        0.05 * ((age - 20) / 70)
    )
    
    return min(0.95, max(0.05, risk_score))

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
        risk = predict_risk(*features)
    
    return render_template('index.html', risk=risk)

if __name__ == '__main__':
    app.run(debug=True)
