"""TFP URL Configuration

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
from account.views import (index_login_view)
from designers.views import (designer_dashboard,add_product,base,update,registration,edit_info)
from customers.views import (customer_registration)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_login_view, name="index"),
    path('designer',designer_dashboard, name='designer_dashboard'),
    path('addPrd',add_product, name='addPrd'),
    path('base',base),
    path('update',update, name='update'),
    path('register',registration, name='register'),
    path('edit_info',edit_info, name='edit_info'),
    path('customer_registraion',customer_registration, name='customer_registration')
]
