from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from designers.models import Product


class MyAccountManager(BaseUserManager):
    def create_user(self, user_name, mobile, email, password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not mobile:
            raise ValueError("User must have a mobile Number")
        user = self.model(
            email=self.normalize_email(email),
            mobile=mobile,
            user_name=user_name,
        )
        user.is_varified = False
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, user_name, mobile,email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            mobile=mobile,
            user_name=user_name,

        )
        user.is_admin = True
        user.is_varified = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=False)
    username = models.CharField(max_length=60, unique=False, blank=True)
    mobile = models.CharField(max_length=13, blank=False, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_varified = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_designer = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile", "username"]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-last_login','-date_joined']



class Designer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=155,null=True,blank=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=15,unique=True)
    bio = models.TextField()
    logo = models.ImageField(upload_to='designer/logo')
   

    def __str__(self):
        return self.name
    
    
    def get_products(self):
        return Product.objects.filter(designer=self)

class CustomerProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=155,null=True,blank=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=15,unique=True)
    house = models.CharField(max_length=25,unique=False)
    landmark = models.CharField(max_length=25,unique=False)
    city = models.CharField(max_length=25,unique=False)
    pincode = models.CharField(max_length=6,unique=False)

    def __str__(self):
        return self.name

