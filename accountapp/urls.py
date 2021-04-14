from django.urls import path

from accountapp.views import hello

app_name = "accountapp"

urlpatterns = [
    path('hello/', hello, name='hello')
]