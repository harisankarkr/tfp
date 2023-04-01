from django.db import models


#user basic model for login
# class User(models.Model):
#     username = models.CharField(max_length=60, unique=False, blank=False)
#     email = models.EmailField(verbose_name="email", max_length=60, primary_key=True, unique=True, blank=False)
#     mobile = models.CharField(max_length=13, blank=False, unique=True)
#     password = models.CharField(max_length=12,blank=False, unique=False)

#     logo = models.ImageField(blank=False)
#     bio = models.CharField(max_length=200, blank=False)

#     house = models.CharField(max_length=30, blank=False)
#     landmark = models.CharField(max_length=30, blank=False)
#     city = models.CharField(max_length=30, blank=False)
#     pincode = models.CharField(max_length=6, blank=False)

#     is_designer = models.BooleanField(default=False) 