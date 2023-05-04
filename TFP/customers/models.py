from django.db import models
from account.models import Designer
from account.models import User
from designers.models import Product

# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user}'s Wishlist"


# order model
class Order(models.Model):
    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    size = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    from_address = models.CharField(max_length=255)
    to_address = models.CharField(max_length=255)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"{self.customer} - {self.product} ({self.size}) - {self.status}"
