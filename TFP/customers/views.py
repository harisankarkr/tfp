from django.shortcuts import render

# Create your views here.

# customer registration page view
def customer_registration(request):
    return render(request,'customerReg.html',{})
