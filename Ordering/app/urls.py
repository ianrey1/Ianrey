from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('home/', views.home, name='home'), 
    path('', views.custom_login_view, name='login'),

    path('records/', views.records, name='records'),
]
