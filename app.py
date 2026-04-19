from flask import Flask, render_template, request, jsonify
from questions import questions
from analyzer import analyze_answer
import random

app = Flask(__name__)

history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_question/<category>")
def get_question(category):
    q = random.choice(questions[category])
    return jsonify({"question":q})

@app.route("/submit", methods=["POST"])
def submit():

    data = request.json
    question = data["question"]
    answer = data["answer"]

    result = analyze_answer(answer, question)

    history.append({
        "question":question,
        "answer":answer,
        "score":result["score"]
    })

    return jsonify(result)

@app.route("/history")
def get_history():
    return jsonify(history)

if __name__ == "__main__":
    app.run(debug=True)
