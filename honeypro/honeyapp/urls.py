from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('oil/', views.oil_page, name='oil_page'),
     
]