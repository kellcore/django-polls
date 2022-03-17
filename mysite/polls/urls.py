# URLConf

# point the root URLconf at the polls.url module
from django.urls import include, path
from django.contrib import admin

from . import views

# map the view to a url
urlpatterns = [
    path('', views.index, name='index')
]

