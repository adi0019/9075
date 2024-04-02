from flask import Flask, request, render_template, jsonify
from flask import Flask, request, jsonify
from Model import SpellCheckerModule

app = Flask(__name__)
spell_checker_module = SpellCheckerModule()



@app.route('/')
def index():
    # return render_template('index.html')
    return "Hello World!"


@app.route('/spell', methods=['POST','GET'])
def spell():
   # return "Hello World!"
    if request.method=='POST':
  # cgpa = request.form.get('cgpa')
        text = request.form['text']
        corrected_text = spell_checker_module.correct_spell(text)

        return jsonify({'corrected text': corrected_text})



# python main
if __name__ == "__main__":
    app.run()
