import pandas as pd
import joblib
from feature_extraction import extract_features
from flask import Flask, request, render_template

app = Flask(__name__)

def predict_URL(URL):
    model = joblib.load('phishing_model.pkl')
    features = extract_features(URL)
    features_df = pd.DataFrame([features])
    prediction = model.predict(features_df)[0]
    return prediction

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    URL = request.form['URL']
    result = predict_URL(URL)
    result_text = "Phishing URL" if result == 1 else "Legitimate URL"
    return render_template('results.html', url=URL, result=result_text)

if __name__ == '__main__':
    app.run(debug=True)
