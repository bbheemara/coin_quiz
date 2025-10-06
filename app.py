from flask import Flask,render_template,url_for, session,redirect,request
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

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    coins = session.get("score", 0)
    streak = session.get("streak", 0)
    if "score" not in session:
        session["score"] = 0
    if "streak" not in session:
        session["streak"] = 0
    if "q_index" not in session:
        session["q_index"] = 0

    q_index = session["q_index"]

    if q_index >= len(questions):
        return redirect(url_for("result"))

    q = questions[q_index]

    if request.method == "POST":
        selected = request.form.get('choice')
        if selected == q["correct"]:
            coins = session["score"] + 10
            streak = session["streak"] + 1

            session["score"] += 10
            session["streak"] += 1
        else:
            session["streak"] = 0

        session["q_index"] = q_index + 1
        return redirect(url_for('quiz'))
    coins = session.get("score", 0)
    streak = session.get("streak", 0)

    return render_template("quiz.html",coins=coins,streak=streak, q=q, q_index=q_index)
    

@app.route('/result')
def result():
    total_score = session["score"]
    streak = session["streak"]
    if total_score>=20:
        msg = "Wow So Lucky!"
    else:
        msg = "Unlucky! same as me :("    
    session["score"] = 0
    session["streak"] = 0
    session["q_index"] = 0

    return render_template('result.html',score=total_score,streak=streak,msg=msg)

if __name__ == '__main__':
    
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
