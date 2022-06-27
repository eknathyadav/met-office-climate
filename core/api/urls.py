from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('regions-list/', views.regions_list),
    path('regions-list/<str:parameter_name>/',
         views.get_regions_parameter),
    path('region-climate/<str:region_name>/', views.get_region),
    path('region-climate/<str:region_name>/<str:parameter_name>/',
         views.get_region_parameter),
]
