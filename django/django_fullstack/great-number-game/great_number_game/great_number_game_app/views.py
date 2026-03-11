from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):
    if 'target' not in request.session:
        request.session['target'] = random.randint(1, 100)
        request.session['attempts'] = 0 
        request.session['winners'] = request.session.get('winners', []) 

    result = request.session.get('result')
    attempts = request.session.get('attempts')
    print(f"Target: {request.session['target']}")
    return render(request, 'numbergame.html', {'result': result, 'attempts': attempts})

def guess(request):
    
    request.session['attempts'] += 1
    user_guess = int(request.POST['guess'])
    target = request.session['target']

    if user_guess == target:
        request.session['result'] = 'correct'
    elif request.session['attempts'] >= 5:
        request.session['result'] = 'lose'
    elif user_guess < target:
        request.session['result'] = 'too_low'
    else:
        request.session['result'] = 'too_high'

    return redirect('/')

def save_leaderboard(request):

    name = request.POST['name']
    winner_data = {'name': name, 'attempts': request.session['attempts']}
    
    winners_list = request.session.get('winners', [])
    winners_list.append(winner_data)
    request.session['winners'] = winners_list
    
    return redirect('/leaderboard')

def leaderboard(request):
    return render(request, 'leaderboard.html', {'winners': request.session.get('winners', [])})

def reset(request):
    winners = request.session.get('winners')
    request.session.clear()
    request.session['winners'] = winners
    return redirect('/')