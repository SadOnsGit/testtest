# myapp/urls.py

from django.urls import path
from .views import login_view

app_name = 'index'

urlpatterns = [
    path('login/', login_view, name='login_view'),
]