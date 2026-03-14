from django.db import models
import re
import datetime
import bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
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
        users_count = User.objects.count();
        user_level = 1
        if users_count == 0:
            user_level = 9
        user = User.objects.create(first_name=first_name , last_name=last_name , email=email , password=password_hashed , user_level = user_level)
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
    
    def get_user(self, post_data):
        email = post_data.get('email' , '')
        return User.objects.filter(email=email).first()

class MassageValidator(models.Manager):
    def validate_data(self, post_data):
        errors={}
        content = post_data['content']
        if len(content) == 0:
            errors['content'] = "massage content can't be empty!"

class User(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    description = models.TextField(null=True)
    user_level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserValidator()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Massage(models.Model):
    content = models.TextField()
    massage_for_user = models.ForeignKey(User, related_name="massages_for", on_delete = models.CASCADE)
    massage_from_user = models.ForeignKey(User, related_name="massages_from", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MassageValidator()

