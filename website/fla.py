from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)  # Enable CORS for all routes

# Load the pipeline from the file
pipeline_path = r'D:\Dev\DevPfa\Model\my_pipeline.pkl'
with open(pipeline_path, 'rb') as f:
    pipe = pickle.load(f)


# Define a function to ask questions using the loaded pipeline and show only the first answer
def ask_question(question):

    prediction = pipe.run(
        query=question,
        params={
            "Retriever": {"top_k": 10},
            "Reader": {"top_k": 5}
        }
    )
    first_answer = prediction["answers"][0].answer
    return first_answer

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
