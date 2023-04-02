from pyexpat.errors import messages
from django.shortcuts import render, redirect
from account.models import Designer


# Create your views here.

# designer dashboard view
def designer_dashboard(request):
    user = request.user
    designer = Designer.objects.get(user=user)
    return render(request, "designerEdit.html", {'designer': designer})

# add product view
def add_product(request):
    return render(request,'addPrd.html',{})

# base html
def base(request):
    return render(request,'designer_base.html',{})

# update stock view
def update(request):
    return render(request,'stockMan.html',{})

# designer registration page view
def designer_registration(request):
    
    return render(request,'DesigReg.html',{})

# edit basic info of designer(dp and logo)
def edit_info(request):
    return render(request,'editInfo.html',{})



