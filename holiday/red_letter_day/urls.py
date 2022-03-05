from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('state', views.state, name='state'),
    path('national', views.national, name='national'),
    path('professional', views.professional, name='professional')
]