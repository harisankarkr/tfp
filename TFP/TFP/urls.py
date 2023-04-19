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

from django.conf import settings
from django.contrib import admin
from django.urls import path
from account.views import (index_login_view, registration, user_login, logout_view,)
from designers.views import (update_stock,delete_product_view,delete_product,edit_designer_profile,designer_dashboard,add_product_view,add_product,base,update,designer_registration,edit_info,)
from customers.views import (all_products,men_topwear,product_detail,userpage2,customer_dashboard,userpage1,user_profile,edit_customer_address)
from django.conf.urls.static import static

urlpatterns = [

    # admin
    path('admin/', admin.site.urls),
    # index
    path('', index_login_view, name="index"),

    # ----------------------------------------------------------------------------------------------------------
    # registration and login

    # unwanted
    path('register',designer_registration, name='register'),
    # registration
    path('registration',registration, name='registration'),
    # login
    path('user_login',user_login, name='user_login'),
    # logout
    path('logout_view', logout_view, name='logout_view'),

    # ------------------------------------------------------------------------------------------------------------
    # designer url's

    # desginer dashboard
    path('designer',designer_dashboard, name='designer_dashboard'),
    # designer base
    path('base',base),
    # edit profile - designer
    path('edit_info',edit_info, name='edit_info'),
    # edit designer profile - function
    path('edit_designer_profile',edit_designer_profile, name="edit_designer_profile"),

    
    # --------------------------------------------------------------------------------------------------------------
    # product url's

    # add new product
    path('addPrd',add_product_view, name='addPrd'),
    # add new product function
    path('add_product',add_product, name='add_product'),
    # add new product
    path('delete_product_view',delete_product_view, name='delete_product_view'),
    # delete product function
    path('product/<int:pk>/delete/', delete_product, name='delete_product'),
    # update product stock 
    path('update',update, name='update'),
    # udate product stock funstion
    #path('<int:pk>/update_stock/', update_stock, name='update_stock'),
    path('update/<int:pk>/', update_stock, name='update'),
    #take all products from db to user page 
    path('all_products/', all_products, name='all_products'),
    # product detail
    path('product/<int:pk>/',product_detail, name='product_detail'),

    # view men's top wear
    path('men_topwear', men_topwear , name='men_topwear'),




# -------------------------------------------------------------------------------------------------
    # customer url's

    # customer dashboard
    path('customer_dashboard',customer_dashboard, name='customer_dashboard'),
    # customer user page 1
    path('userpage1',userpage1, name='userpage1'),
    # customer user page 2
    path('userpage2',userpage2, name='userpage2'),
    # customer user page 1
    path('user_profile',user_profile, name='user_profile'),
    # edit customer address function
    path('edit_customer_address',edit_customer_address, name='edit_customer_address'),
    


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
