from django import forms


from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import User, Designer, customer

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'mobile', 'user_name', 'password1', 'password2')

class DesignerRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=30, help_text='Required. Enter a valid email address.')
    name = forms.CharField(max_length=30, required=True)
    phone = forms.CharField(max_length=15, required=True)
    bio = forms.CharField(widget=forms.Textarea)
    logo = forms.ImageField(required=True)

    class Meta:
        model = Designer
        fields = ('email', 'phone', 'password1', 'password2', 'name', 'bio', 'logo')
