from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from designers.forms import ProductForm
from account.models import Designer


# Create your views here.

# designer dashboard view
def designer_dashboard(request):
    return render(request, "designerEdit.html", {})

# add product view
def add_product_view(request):
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



# =====================================================================================================

# add product
# ________________

# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect

# @login_required
# def add_product(request):
#     if not request.user.is_designer:
#         return redirect('designer_dashboard') 

#     if request.method == 'POST':
#         print(request.POST)
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.errors)
#             try:
#                 product = form.save(commit=False)
#                 product.designer = request.user
#                 print(product.designer)
#                 product.save()
#                 form.save_m2m()
#                 print('form not valid')
#                 return redirect('designer_dashboard', prd_name=product.prd_name, designer=product.designer)
#             except Exception as e:
#                 print(e)
#                 return HttpResponse('Error saving product')

#     else:
#         form = ProductForm()
#     return render(request, 'addPrd.html', {'form': form})

# =====================================================================================================

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Designer, Product
from .forms import ProductForm

@login_required
def add_product(request):
    if not request.user.is_designer:
        return redirect('designer_dashboard')

    designer = Designer.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.designer = designer
            product.save()
            form.save_m2m()
            return redirect('designer_dashboard')
    else:
        form = ProductForm()

    return render(request, 'addPrd.html', {'form': form})
