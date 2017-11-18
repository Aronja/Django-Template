"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

'''include allows references from other urls'''

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]

'''the url function takes 4 arguments; regex, view, kwargs and name; the first
two are required
regex are regular expressions, which are matching url patterns
they are not searching for the domain name or or GET/POST request
e.g.: an regex will search for in Domain/myapp for my app and
in Domain/myapp/?page=3 still for myapp; regex are compiled the first time the
URLconf module is loaded; unless the looksups aren't too complex, they're
very fast'''

'''the view function takes an Httpresponse'''
