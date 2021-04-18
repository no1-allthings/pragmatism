from django.urls import path

from accountapp.views import hello, AccountCreateView

app_name = "accountapp"

urlpatterns = [
    path('hello/', hello, name='hello'),

    path('create/', AccountCreateView.as_view(), name='create')
]