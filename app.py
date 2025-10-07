from flask import Flask, render_template, request,jsonify
import pickle
import numpy as np
import pandas as pd


app = Flask(__name__)

# ---- Load Spam SMS model and vectorizer ----
with open('model (1).pkl', 'rb') as f:
    spam_model = pickle.load(f)

with open('vectorizer (1).pkl', 'rb') as f:
    spam_vectorizer = pickle.load(f)

# ---- Load IPL Win Predictor pipeline ----
with open('pipe.pkl', 'rb') as f:
    ipl_pipe = pickle.load(f)

# ---- Routes ----
@app.route('/')
def home():
    return render_template('page.html')  # Home page with navigation links

@app.route('/spam')
def spam_page():
    return render_template('m1.html')  # Spam SMS predictor page

@app.route('/predict_sms', methods=['POST'])
def predict_sms():
    data = request.get_json()
    message = data.get('message', '')
    if message.strip() == '':
        return {"prediction": "Please enter a message."}

    # Vectorize and predict
    message_vector = spam_vectorizer.transform([message])
    prediction = spam_model.predict(message_vector)[0]
    result = "Spam" if prediction == 1 else "Ham"
    return {"prediction": result}

@app.route('/ipl')
def ipl_page():
    return render_template('m2.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract input values
        batting_team = str(data['batting_team'])
        bowling_team = str(data['bowling_team'])
        city = str(data['city'])
        runs_left = int(data['runs_left'])
        balls_left = int(data['balls_left'])
        wickets = int(data['wickets'])
        total_runs_x = int(data['total_runs_x'])
        crr = float(data['crr'])
        rrr = float(data['rrr'])

        # Create DataFrame with the same column names as training
        input_df = pd.DataFrame([{
            "batting_team": batting_team,
            "bowling_team": bowling_team,
            "city": city,
            "runs_left": runs_left,
            "balls_left": balls_left,
            "wickets": wickets,
            "total_runs_x": total_runs_x,
            "crr": crr,
            "rrr": rrr
        }])

        # Predict probability of batting team win
        prediction_value = ipl_pipe.predict_proba(input_df)[0][1]
        batting_win = round(float(prediction_value) * 100, 2)

        return jsonify({
            "batting_team_win_probability": batting_win
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
