from django.shortcuts import render

# Create your views here.

def greeting(request):

    return render(request, "myapp/index.html",)