from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import User, Designer, CustomerProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Enter a valid email address.')
    mobile = forms.CharField(max_length=13, help_text='Required. Enter a valid mobile number.')
    username = forms.CharField(max_length=60, help_text='Required. Enter a user name.')
    is_designer = forms.BooleanField(required=False, label='Are you a designer?')

    class Meta:
        model = User
        fields = ('email', 'mobile', 'user_name', 'password1', 'password2', 'is_designer')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.is_designer = self.cleaned_data['is_designer']
        if commit:
            user.save()
        if user.is_designer:
            designer = Designer.objects.create(
                user=user, 
                name = user.username,
                email=user.email, 
                phone=user.mobile
            )
            designer.save()
        else:
            customer = CustomerProfile.objects.create(
                user=user, 
                name=user.username,
                email=user.email, 
                phone=user.mobile
            )
            customer.save()
        return user
