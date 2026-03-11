from django.shortcuts import render
from time import localtime, strftime
# Create your views here.

def index(request):
    context = {
        "current_time": strftime("%I:%M %p", localtime()),
        "current_date": strftime("%b %d, %Y", localtime()),
    }
    return render(request, 'index.html', context)