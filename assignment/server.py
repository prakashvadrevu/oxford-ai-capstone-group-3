from flask import Flask, request, jsonify, render_template
from app import answer_question

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    history = data.get('history', [])
    
    # Assuming the `history` is used in some way by `answer_question`, otherwise we ignore it for now
    answer = answer_question(question, history)

    print("********** answer ************")
    print(answer)
    
    return jsonify(answer=answer)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
