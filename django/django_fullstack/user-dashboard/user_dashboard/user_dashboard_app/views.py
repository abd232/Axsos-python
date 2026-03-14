from django.shortcuts import render, redirect, HttpResponse
from .models import User, Massage
from time import gmtime, strftime
# Create your views here.
def index(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        errors = User.objects.validate_data(request.POST)
        if errors:
            context={
                'errors' : errors,
            }
            return render(request , 'regesteration.html' , context=context)
        else:
            user = User.objects.create_user(request.POST)
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['user_id'] = user.id
            if user.user_level == 9:
                return redirect('/admin-dashboard')
            return redirect('/dashboard')
    else:
        return render(request, "regesteration.html")
    
def login(request):
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)
        if errors:
            context={
                'errors' : errors,
            }
            return render(request , 'login.html' , context=context)
        else:
            user = User.objects.get_user(request.POST)
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['user_id'] = user.id
            if user.user_level == 9:
                return redirect('/admin-dashboard')
            return redirect('/dashboard')
    else:
        return render(request, "login.html")

def logout(request):
    request.session.clear()
    return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/register')
    
    user = User.objects.get(id = request.session['user_id'])

    if not user:
        return redirect('/register')
    
    users = User.objects.all()

    context = {'users' : users}

    if user.user_level == 9:
        return render(request, 'admin_dashboard.html', context=context)
    
    return render(request, 'dashboard.html', context=context)

def profile(request, id):
    if 'user_id' not in request.session:
        return redirect('/register')
    
    user = User.objects.get(id = id)

    if not user:
        return redirect('/register')
    
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'user_id' : user.id,
        'created_at' : strftime("%B %dth %Y.", user.created_at.timetuple()),
        'email' : user.email,
        'description' : user.description,
        'massages' : user.massages_for.all()
    }

    return render(request, "profile.html", context = context)

def massage(request, for_user_id):   
    if 'user_id' not in request.session:
        return redirect('/register')
    
    user = User.objects.get(id = request.session["user_id"])

    if not user:
        return redirect('/register')

    if request.method != 'POST':
        return redirect('/')
    
    errors = Massage.objects.validate_data(request.POST)

    if errors:
        context={
            'errors' : errors,
        }
        return HttpResponse("post content can't be empty")
    else:
        for_user = User.objects.get(id = for_user_id)
        from_user = User.objects.get(id = request.session['user_id'])
        Massage.objects.create(content = request.POST['content'], massage_from_user = from_user, massage_for_user = for_user)

        return redirect(f"/users/show/{for_user_id}")