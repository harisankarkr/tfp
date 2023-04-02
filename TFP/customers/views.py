from django.shortcuts import render

from account.models import CustomerProfile


# customer registration page view
def customer_registration(request):
    return render(request,'customerReg.html',{})

# customer base
def customer_dashboard(request):
    return render(request,'user1.html',{})

# customer - user page 1
def userpage1(request):
    return render(request,'customer_base.html',{})

# user profile
def user_profile(request):
    user = request.user
    customer = CustomerProfile.objects.get(user=user)
    return render(request, "userprofile.html", {'customer': customer})