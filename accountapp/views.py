from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import Hello


def hello(request):
    if request.method == "POST":
        temp = request.POST.get('hello_input')
        new_hello = Hello()
        new_hello.text = temp
        new_hello.save()
        return render(request, 'accountapp/hello.html', context={'hello_output': new_hello})
    else:
        return render(request, 'accountapp/hello.html', context={'hello_output': 'GET!!'})