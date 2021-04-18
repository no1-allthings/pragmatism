from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

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

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello')
    template_name = 'accountapp/create.html'

