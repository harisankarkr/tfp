from django import forms
# from django.contrib.auth.models import User
from account.models import Designer,User


# designer registration
class DesignerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Designer
        fields = ['name', 'email', 'phone', 'bio', 'logo']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password

    def save(self, commit=True):
        designer = super().save(commit=False)
        designer.user = User.objects.create_designer(
            user_name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            mobile=self.cleaned_data['phone'],
            password=self.cleaned_data['password']
        )
        if commit:
            designer.save()
        return designer


# designer login
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class DesignerLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)