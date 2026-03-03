from django.shortcuts import render
from time import gmtime, strftime
# Create your views here.

def index(request):
    context = {
        "current_time": strftime("%I:%M %p", gmtime()),
        "current_date": strftime("%b %d, %Y", gmtime()),
    }
    return render(request, 'index.html', context)