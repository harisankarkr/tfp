from django.db import models

# from account.models import Designer


# Create your models here.



# product table
class Product(models.Model):
    designer = models.ForeignKey('account.Designer', on_delete=models.CASCADE, null=True)
    prd_name = models.CharField(max_length=255)
    category1 = models.CharField(max_length=255)
    category2 = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fit = models.CharField(max_length=255)
    care = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    occasion = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to='product_images/')
    image2 = models.ImageField(upload_to='product_images/', blank=True)
    image3 = models.ImageField(upload_to='product_images/', blank=True)
    image4 = models.ImageField(upload_to='product_images/', blank=True)
    small = models.PositiveIntegerField()
    medium = models.PositiveIntegerField()
    large = models.PositiveIntegerField()
    extra_large = models.PositiveIntegerField()

    class Meta:
        unique_together = ('prd_name', 'designer')

    def __str__(self):
        return self.prd_name
