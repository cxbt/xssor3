"""xssor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.urls import re_path
from django.contrib import admin
from xssor.index.views import index, cmd_create, cmd, \
                            probe_create, probe_js, probe_txt, probe_status
from django.views.generic.base import RedirectView

urlpatterns = [
    re_path(r'^adminofwhatidonotcare/', admin.site.urls),
    re_path(r'^$', index),
    re_path(r'^favicon.ico$', RedirectView.as_view(url='/s/favicon.ico')),
    re_path(r'^cmd/create/?$', cmd_create),
    re_path(r'^cmd/?$', cmd),
    re_path(r'^probe/create/?$', probe_create),
    re_path(r'^probe/(?P<pid>\w+).js/?$', probe_js),
    re_path(r'^probe/(?P<pid>\w+).txt/?$', probe_txt),
    re_path(r'^probe/status/?$', probe_status),
]

