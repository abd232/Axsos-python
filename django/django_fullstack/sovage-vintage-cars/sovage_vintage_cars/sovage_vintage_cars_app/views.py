from django.shortcuts import render , redirect
from .models import User, Car

# Create your views here.
def index(request):
    return render(request , 'index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.validate_data(request.POST)
        if errors:
            context={
                'errors' : errors,
            }
            return render(request , 'index.html' , context=context)
        else:
            user = User.objects.create_user(request.POST)
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['user_id'] = user.id
            return redirect('/cars')

def log_in(request):
    if request.method == 'POST':
        errors = User.objects.validate_login(request.POST)
        if errors:
            context={
                'errors' : errors,
            }
            return render(request , 'index.html' , context=context)
        else:
            user = User.objects.get_user_by_email(request.POST)
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['user_id'] = user.id
            return redirect('/cars')
    return redirect('/')

def log_out(request):
    request.session.clear()
    return redirect('/')

def cars(request):
    if not 'user_id' in request.session:
        return redirect ('/')
    user = User.objects.get(id=request.session['user_id'])

    if not user:
        return redirect('/')

    cars = Car.objects.all()
    carsList = []
    for car in cars:
        carDTO = {}
        carDTO['car_id'] = car.id
        carDTO['year'] = car.year
        carDTO['model'] = car.model
        carDTO['dealer'] = f"{car.posted_by.first_name} {car.posted_by.last_name}"
        carDTO['is_for_user'] = car.posted_by.id == user.id
        if car.bought_by:
            carDTO['is_soldout'] = True
        else:
            carDTO['is_soldout'] = False
        carsList.append(carDTO)

    return render(request , 'cars.html', {'cars' : carsList })

def newcar(request):
    if not 'user_id' in request.session:
        return redirect ('/')
    user = User.objects.get(id=request.session['user_id'])

    if not user:
        return redirect('/')
    
    if request.method == 'POST':
        errors = Car.objects.validate_data(request.POST)
        if errors:
            context={
                'errors' : errors,
            }
            return render(request , 'newcar.html' , context=context)
        
        Car.objects.create_car(request.POST, user)
        return redirect('/cars')
    
    return render(request, 'newcar.html')

def car(request, id):
    if not 'user_id' in request.session:
        return redirect ('/')
    user = User.objects.get(id=request.session['user_id'])

    if not user:
        return redirect('/')
    
    car = Car.objects.get(id = id)
    print(car.bought_by.last_name)
    return render(request, 'car-details.html', {'car':car})

def buy_car(request, id):
    if not 'user_id' in request.session:
        return redirect ('/')
    user = User.objects.get(id=request.session['user_id'])

    if not user:
        return redirect('/')
    
    car = Car.objects.get(id = id)

    car.bought_by = user
    car.save()
    return redirect(f"/cars/{id}")

def unbuy_car(request, id):
    if not 'user_id' in request.session:
        return redirect ('/')
    user = User.objects.get(id=request.session['user_id'])

    if not user:
        return redirect('/')
    
    car = Car.objects.get(id = id)

    car.bought_by = None
    car.save()
    return redirect(f"/cars/{id}")

def edit_car(request, id):
    if not 'user_id' in request.session:
        return redirect ('/')
    user = User.objects.get(id=request.session['user_id'])

    if not user:
        return redirect('/')
    
    car = Car.objects.get(id = id)

    if request.method == 'POST':
        errors = Car.objects.validate_data(request.POST)
        if errors:
            context={
                'errors' : errors,
                'car' : car,
            }
            return render(request , 'edit-car.html' , context=context)
        
        Car.objects.edit_car(request.POST, id)
        return redirect('/cars')


    return render(request, 'edit-car.html', {'car' : car, 'car_id' : id})
    
def remove_car(request, id):
    if not 'user_id' in request.session:
        return redirect ('/')
    user = User.objects.get(id=request.session['user_id'])

    if not user:
        return redirect('/')
    
    car = Car.objects.get(id = id)
    car.delete()

    return redirect('/cars')

def user_purcheses(request, id):
    if not 'user_id' in request.session:
        return redirect ('/')
    user = User.objects.get(id=id)

    if not user:
        return redirect('/')

    cars = Car.objects.filter(bought_by = user)
    carsList = []
    for car in cars:
        carDTO = {}
        carDTO['car_id'] = car.id
        carDTO['year'] = car.year
        carDTO['model'] = car.model
        carDTO['seller_contact'] = car.seller_contact
        carDTO['dealer'] = f"{car.posted_by.first_name} {car.posted_by.last_name}"
    return render(request , 'user-purcheses.html', {'cars' : carsList })