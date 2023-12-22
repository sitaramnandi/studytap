"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('place_order/', place_order, name='place_order'),
    path('get_order_status/<int:order_id>/', get_order_status, name='get_order_status'),
    path('update_to_in_progress/<int:order_id>/', update_to_in_progress, name='update_to_in_progress'),
    path('update_to_delivered/<int:order_id>/', update_to_delivered, name='update_to_delivered'),
]
