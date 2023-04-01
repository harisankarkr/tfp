from django.shortcuts import render

# Create your views here.

# designer dashboard view
def designer_dashboard(request):
    return render(request,"designerEdit.html",{})

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
def registration(request):
    return render(request,'DesigReg.html',{})

# edit basic info of designer(dp and logo)
def edit_info(request):
    return render(request,'editInfo.html',{})