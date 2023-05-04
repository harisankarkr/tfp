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
from customers.views import (remove_from_wishlist, create_order, tour_orders)
from customers.views import (add_to_wishlist, wishlist, cart, men_bottomwear, women_fusion, women_ethnic)
from account.views import (index_login_view, registration, user_login, logout_view, error)
from designers.views import (update_stock,delete_product_view,delete_product,edit_designer_profile,designer_dashboard,add_product_view,add_product,base,update,designer_registration,edit_info,)
from customers.views import (designer_profile,all_products,men_topwear,product_detail,userpage2,customer_dashboard,userpage1,user_profile,edit_customer_address)
from django.conf.urls.static import static

urlpatterns = [

    # admin
    path('admin/', admin.site.urls),
    # index
    path('', index_login_view, name="index"),
    
    # error
    path('error', error , name="error"),

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


# ----------------------------------------------------------
    # view men's topwear
    path('men_topwear', men_topwear , name='men_topwear'),
    # view men's bottomwear
    path('men_bottomwear', men_bottomwear , name='men_bottomwear'),
    # view women_fusion
    path('women_fusion', women_fusion , name='women_fusion'),
    # view women_ethnic
    path('women_ethnic', women_ethnic , name='women_ethnic'),
# -----------------------------------------------------------


# ----------------------------------------------------------------------------
    # view designer profile
     path('designer/<int:pk>/', designer_profile, name='designer_profile'),
# -----------------------------------------------------------------------------



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
    

    # whishlist (view , add , remove) 
    path('wishlist', wishlist, name='wishlist'),
    path('add/<int:product_id>', add_to_wishlist, name='add_to_wishlist'),
    path('remove/<int:pk>', remove_from_wishlist, name='remove_from_wishlist'),

    # cart
    path('cart/<int:product_id>', cart, name='cart'),

    # order
    path('create_order/<int:product_id>', create_order, name='create_order'),
    # pending orders
    path('tour_orders', tour_orders, name='tour_orders'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
