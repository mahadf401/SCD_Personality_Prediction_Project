from flask import Flask, render_template, request, jsonify
import threading
import pandas as pd
from pickle import load
from Test import generate_chart

app = Flask(__name__)

# Load the questions from CSV file
questions_df = pd.read_csv('questions.csv')

# Global dictionary for threaded result
result_data = {}

@app.route('/')
def index():

    return render_template(
        'index.html',
        questions=questions_df.to_dict(orient='records')
    )

# Threading function
def threaded_prediction(user_responses_df):

    global result_data

    personality_type, my_sums = generate_chart(user_responses_df)

    result_data["personality_type"] = personality_type
    result_data["labels"] = list(my_sums.columns[0:5])
    result_data["data"] = list(my_sums.values[0][0:5])

@app.route('/submit', methods=['POST'])
def submit():

    user_responses = {}

    for key, value in request.form.items():
        user_responses[key] = value

    # Convert responses into dataframe
    user_responses_df = pd.DataFrame(
        user_responses,
        index=[0]
    )

    user_responses_df = user_responses_df.astype(int)

    # Create thread
    thread = threading.Thread(
        target=threaded_prediction,
        args=(user_responses_df,)
    )

    # Start thread
    thread.start()

    # Wait for thread to finish
    thread.join()

    # Render result page
    return render_template(
        'results.html',
        personality_type=result_data["personality_type"],
        labels=result_data["labels"],
        data=result_data["data"]
    )

# API route for Postman testing
@app.route('/api/test', methods=['GET'])
def api_test():

    return jsonify({
        "message": "API is working successfully"
    })

if __name__ == '__main__':
    app.run(debug=True)