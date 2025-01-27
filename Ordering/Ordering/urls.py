"""
URL configuration for Ordering project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('home/', views.home, name='home'),  # Updated to include '/home/'

    # Ensure login page is the first page when visiting the root URL
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login_redirect'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # The rest of your application routes
    path('add_order/', views.add_order, name='add_order'),
    path('records/', views.records, name='records'),
    path('edit_order/<int:order_id>/', views.edit_order, name='edit_order'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('orders/', views.order_list, name='view_orders'),
]












