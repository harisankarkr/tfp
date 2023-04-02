from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import User, Designer, CustomerProfile
from django.contrib.auth.forms import AuthenticationForm



# registraion form -----------------------------------------------------------------------------------

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Enter a valid email address.')
    mobile = forms.CharField(max_length=13, help_text='Required. Enter a valid mobile number.')
    username = forms.CharField(max_length=60, help_text='Required. Enter a user name.')
    is_designer = forms.BooleanField(required=False, label='Are you a designer?')

    class Meta:
        model = User
        fields = ('email', 'mobile', 'username', 'password1', 'password2', 'is_designer')


# login form ----------------------------------------------------------------------------------------

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=60, help_text='Required. Enter a user name.')
    password = forms.CharField(widget=forms.PasswordInput)