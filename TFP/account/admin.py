from django.contrib import admin

from account.models import User,Designer,CustomerProfile

# Register your models here.
admin.site.register(User)
admin.site.register(Designer)
admin.site.register(CustomerProfile)
