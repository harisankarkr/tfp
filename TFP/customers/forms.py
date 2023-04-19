from django import forms
from account.models import CustomerProfile

# edit customer address
class CustAddressForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ('house', 'landmark','city','pincode')