from django.contrib import admin
from django.conf.urls import url
from . import views
from . import models

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.signIn),
    url(r'^adder$', views.createUser),
    url(r'^exit$', views.goingaway),
    url(r'^dash$', views.renderDash),
    # url(r'^edit$', views.edit),
    # url(r'^deleter$', views.deleter),
    url(r'^look$', views.look),
    url(r'^addTo$', views.addFav),
    url(r'^addQ$', views.addQuote)
]
