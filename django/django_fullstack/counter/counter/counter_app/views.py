from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'visited_time' in request.session:
        request.session['visited_time'] = request.session['visited_time'] + 1
    else:
        request.session['visited_time'] = 1
    
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, 'index.html')

def increment_by_two(request):
    if 'counter' in request.session:
        request.session['counter'] = request.session.get('counter') + 2
    else:
        request.session['counter'] = 2
    return render(request, 'index.html')


def increment(request):
    increment_value = int(request.POST.get('increment_value'))  # Default to 1 if not provided
    if 'counter' in request.session:
        request.session['counter'] = request.session.get('counter') + increment_value
    else:
        request.session['counter'] = increment_value
    return render(request, 'index.html')

def reset(request):
    request.session['counter'] = 0
    return redirect('/')

def destroy(request):
    request.session.clear()
    return redirect('/')
    