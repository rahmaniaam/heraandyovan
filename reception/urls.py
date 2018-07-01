from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'reception'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^add_guest', views.add_guest, name='add_guest'),
]