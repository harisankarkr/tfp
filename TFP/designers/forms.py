from django import forms
from designers.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['prd_name', 'category1', 'category2', 'price', 'fit', 'care', 'material', 'occasion', 'image1', 'image2', 'image3', 'image4', 'small', 'medium', 'large', 'extra_large']

