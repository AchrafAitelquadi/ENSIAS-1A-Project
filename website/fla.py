from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from functions import *

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)  # Enable CORS for all routes

# Load the pipeline from the file

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json['message']
    response = ask_question(user_message)
    return jsonify({'response': response})

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
