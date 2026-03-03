from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
# Create your views here.
def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog with a method named 'create'")

def create(request):
    return redirect('/')

def show(request, num):
    return HttpResponse(f"placeholder to display blog number: {num}")

def edit(request, num):
    return HttpResponse(f"placeholder to edit blog {num}")

def destroy(request, num):
    return redirect('/')

def json(request):
    return JsonResponse({'title': "blogTitle", 'content': "something here"})