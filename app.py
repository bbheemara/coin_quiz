from flask import Flask,render_template,url_for, session,redirect
from questions import questions

app = Flask(__name__)
app.secret_key = "hmmwhatisthiss..."
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start')
def start():
    session["score"] = 0
    session["streak"] = 0
    session["q_index"] = 0
    return redirect(url_for("quiz"))

@app.route('/quiz',methods=["GET", "POST"])
def quiz():
    ques_index = session.get("q_index", 0)



if __name__ == '__main__':
    
    app.run(debug=True)