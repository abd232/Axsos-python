from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return redirect('/shows')
    
def new(request):       
    return render(request, 'add_show.html')