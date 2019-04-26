from django.urls import path
from . import views
urlpatterns = [path('asswetran', views.simple_upload, name='asswetran')]
