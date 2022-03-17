"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# the include() function allows referencing other URLconfs
from django.urls import include, path

urlpatterns = [
    # whenever django encounters include(), it chops off whatever part of the URL matched up to that point -> sends the remaining string to included URLconf for further processing
    # since polls are in their own URLconf (polls/urls.py), they can be placed under "/polls" or "/fun_polls" or "/content/polls" or any other path root, and the app will still work
    # always use include() when you include other URL patterns -> admin.site.urls is the only exception to this!
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
