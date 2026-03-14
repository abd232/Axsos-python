from django.db import models
import re
import datetime
import bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserValidator(models.Manager):
    def validate_data(self, post_data):
        errors={}
        first_name = post_data.get('first_name' , '')
        if len(first_name) <= 2:
            errors['first_name'] = 'First name must be at least 2 character'
        last_name = post_data.get('last_name' , '')
        if len(last_name) <= 2:
            errors['last_name'] = 'Last name must be at least 2 character'
        email = post_data.get('email' , '')
        if not EMAIL_REGEX.match(email):
            errors['email'] = 'Invalid email'
        elif User.objects.filter(email=email).first():
            errors['email'] = 'Email exists already'
        password = post_data.get('password' , '')
        confrim_password=post_data.get('confrim_password' , '')
        if len(password) <= 8 :
            errors['password'] = 'Password must be 8 charecter'
        if password != confrim_password:
            errors['confrim_password'] = 'Password not match'
        return errors
    
    def create_user(self, post_data):
        first_name = post_data.get('first_name' , '')
        last_name = post_data.get('last_name' , '')
        email = post_data.get('email' , '')
        password = post_data.get('password' , '')
        password_hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(first_name=first_name , last_name=last_name , email=email , password=password_hashed)
        return user
    
    def validate_login(self , post_data):
        errors={}
        email = post_data.get('email' , '')
        password = post_data.get('password' , '')
        user = User.objects.filter(email=email).first()
        if user:
            user_password = user.password
            if bcrypt.checkpw(password.encode(), user_password.encode()):
                return {}
        errors['user'] = 'Email or password not valid'

        return errors
    
    def get_user_by_email(self, post_data):
        email = post_data.get('email' , '')
        return User.objects.filter(email=email).first()

class CarValidator(models.Manager):
    def validate_data(self, post_data):
        errors={}
        price = post_data.get('price', 0)
        model = post_data.get('model' , '')
        make = post_data.get('make' , '')
        year = post_data.get('year' , 0)
        seller_contact = post_data.get('seller_contact', '')
        description = post_data.get('description', '')
        if price == 0:
            errors['price'] = "price can't be empty or zero"
        if len(model) == 0:
            errors['model'] = "model can't be empty"
        if len(make) == 0:
            errors['make'] = "make can't be empty"
        if year == 0:
            errors['year'] = "year can't be empty or zero"
        x = datetime.datetime.now()
        if int(year) > x.year:
            errors['year'] = "year can't be in future"
        if len(seller_contact) == 0:
            errors['seller_contact'] = "sellect contact can't be empty"
        if len(description) < 10:
            errors['description'] = "description must have at least 10 characters"
        
        return errors;

    def create_car(self, post_data, user):
        price = post_data.get('price', 0)
        model = post_data.get('model' , '')
        make = post_data.get('make' , '')
        year = post_data.get('year' , 0)
        posted_by = user
        seller_contact = post_data.get('seller_contact', '')
        description = post_data.get('description', '')
        return Car.objects.create( price = price, model = model, make = make, year = year, seller_contact = seller_contact,posted_by = posted_by, description = description)
    
    def edit_car(self, post_data, id):
        car = Car.objects.get(id=id)
        car.price = post_data.get('price', 0)
        car.model = post_data.get('model' , '')
        car.make = post_data.get('make' , '')
        car.year = post_data.get('year' , 0)
        car.seller_contact = post_data.get('seller_contact', '')
        car.description = post_data.get('description', '')
        return car.save()

        

        
        




class User(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserValidator()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Car(models.Model):
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    make = models.CharField(max_length=60)
    year = models.IntegerField()
    description = models.TextField()
    seller_contact = models.CharField(max_length=20)
    posted_by = models.ForeignKey(User, related_name="cars_posted", on_delete = models.CASCADE)
    bought_by = models.ForeignKey(User, related_name="cars_bought", on_delete = models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CarValidator()