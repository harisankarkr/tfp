from django.contrib import admin
from customers.models import Order
from customers.models import Wishlist


# Register your models here.
admin.site.register(Wishlist)
admin.site.register(Order)

