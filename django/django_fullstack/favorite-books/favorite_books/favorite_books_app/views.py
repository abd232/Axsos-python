from pyexpat.errors import messages
import bcrypt
from django.shortcuts import render, redirect
from .models import User
# Create your views here.

def login_register(request):
    return render(request, 'login_register.html')

def register(request):
    if request.method != 'POST':
        return redirect('/')
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0: 
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        # create the 
        userpw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = userpw_hash
        )
        request.session['user_id'] = User.objects.last().id
        request.session['first_name'] = User.objects.last().first_name
        request.session['logged_in'] = True
        return redirect('/books')
    
def login(request):
    if request.method != 'POST':
        return redirect('/')
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0: 
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        logged_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = logged_user.id
        request.session['first_name'] = logged_user.first_name
        request.session['logged_in'] = True
        return redirect('/books')
    
def logout(request):
    request.session.flush()
    return redirect('/')

def books(request):
    if 'logged_in' not in request.session:
        return redirect('/')
    return render(request, 'books.html')