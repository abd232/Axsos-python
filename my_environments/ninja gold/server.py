from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "ninja_secret"  # needed for session

@app.route("/")
def index():
    # initialize session variables if not set
    if "gold" not in session:
        session["gold"] = 0
        session["activities"] = []
        session["moves"] = 0
    return render_template("index.html", gold=session["gold"], activities=session["activities"])

@app.route("/process_money", methods=["POST"])
def process_money():
    building = request.form["building"]

    # gold ranges for each building
    ranges = {
        "farm": (10, 20),
        "cave": (5, 10),
        "house": (2, 5),
        "casino": (-50, 50)
    }

    # pick random gold amount
    gold_earned = random.randint(ranges[building][0], ranges[building][1])
    session["gold"] += gold_earned
    session["moves"] += 1

    # activity log
    if gold_earned >= 0:
        activity = f"Earned {gold_earned} golds from the {building}!"
        color = "green"
    else:
        activity = f"Lost {abs(gold_earned)} golds at the {building}..."
        color = "red"

    session["activities"].insert(0, [activity, color])  # most recent first

    # sensei bonus: winning condition
    if session["moves"] >= 15 or session["gold"] >= 500:
        session["game_over"] = True

    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)