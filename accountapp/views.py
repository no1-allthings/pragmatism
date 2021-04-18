from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import Hello


def hello(request):
    if request.method == "POST":
        temp = request.POST.get('hello_input')
        new_hello = Hello()
        new_hello.text = temp
        new_hello.save()
        return HttpResponseRedirect(reverse('accountapp:hello'))
    else:
        hello_list = Hello.objects.all()
        return render(request, 'accountapp/hello.html', context={'hello_list': hello_list})