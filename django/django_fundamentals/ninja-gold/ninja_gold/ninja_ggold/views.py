from django.shortcuts import render,redirect
import random

# Create your views here.
def index(request):
    if "gold" not in request.session:
        request.session["gold"] = 0
        request.session["activities"] = []
        request.session["moves"] = 0

    return render(request, 'index.html')


def process_money(request):
    building = request.POST["building"]

    # gold ranges for each building
    ranges = {
        "farm": (10, 20),
        "cave": (5, 10),
        "house": (2, 5),
        "casino": (-50, 50)
    }

    # pick random gold amount
    gold_earned = random.randint(ranges[building][0], ranges[building][1])
    request.session["gold"] += gold_earned
    request.session["moves"] += 1

    # activity log
    if gold_earned >= 0:
        activity = f"Earned {gold_earned} golds from the {building}!"
        color = "green"
    else:
        activity = f"Lost {abs(gold_earned)} golds at the {building}..."
        color = "red"

    request.session["activities"].insert(0, [activity, color])  # most recent first

    # sensei bonus: winning condition
    if request.session["moves"] >= 15 or request.session["gold"] >= 500:
        request.session["game_over"] = True

    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)