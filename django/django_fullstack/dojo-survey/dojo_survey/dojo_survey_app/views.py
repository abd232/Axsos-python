from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    context = {
        'name': request.POST.get('your_name'),
        'location': request.POST.get("location"),
        'favorite_language': request.POST.get("favorite_language"),
        'comment': request.POST.get("comment")
    }
    return render(request, "result.html", context)
