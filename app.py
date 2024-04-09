from flask import Flask, render_template, request, jsonify
import json
import subprocess
app = Flask(__name__)
answers = {}  # Declare answers as a global variable

@app.route('/', methods=['GET', 'POST'])
def ask_questions():
    global answers  # Use the global answers variable

    selected_indirect_questions = [
        {"question": "Would you enjoy spending a quiet afternoon immersed in a novel?", "trait": "LikesReading", "trait2": "Openness"},
        {"question": "Do you often find yourself rearranging your workspace to keep it tidy?", "trait": "IsOrganized", "trait2": "Conscientiousness"},
        {"question": "Would you enjoy attending a large social gathering?", "trait": "IsSocial", "trait2": "Extraversion"},
        {"question": "Do you feel sympathy when you hear about someone's misfortune?", "trait": "IsSympathetic", "trait2": "Agreeableness"},
        {"question": "Do you usually feel nervous when something unexpected happens?", "trait": "GetsNervous", "trait2": "Neuroticism"}
    ]

    if request.method == 'POST':
        answers = {question["trait"]: request.form.get(question["trait"]) for question in selected_indirect_questions}
        print(answers)

        # Write answers to input.json
        with open('input.json', 'w') as f:
            json.dump(answers, f)

    return render_template('question.html', questions=selected_indirect_questions)

@app.route('/output', methods=['GET'])
def show_output():
    with open('output.json', 'r') as f:
        data = json.load(f)
    return render_template('output.html', data=data)
@app.route('/inferenceprocess', methods=['GET'])
def show_inference():
    with open('infrenceprocess.json', 'r') as f:
        data = json.load(f)
    return render_template('inference.html', data=data)

@app.route('/run_processing')
def run_processing():
    subprocess.run(["bash", "-c", "cd ~/expert-system && source venv/bin/activate && python3.9 for.py"])
    return 'Processing executed successfully'

if __name__ == '__main__':
    app.run(debug=True)
