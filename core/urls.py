from django.contrib import admin
from django.urls import include, path
from . import views
app_name = 'core'
urlpatterns = [
    path('', views.extractData, name="extract"),
]
