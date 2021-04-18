from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    if request.method == "POST":
        return render(request, 'accountapp/hello.html', context={'te': 'post!!'})
    else:
        return render(request, 'accountapp/hello.html', context={'te': 'GET!!'})