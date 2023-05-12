from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from designers.forms import ProductForm
from account.models import Designer
from designers.models import Product
from customers.models import Order

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import DesignerProfileForm, ProductForm, StockForm


# Create your views here.

# designer dashboard view
# def designer_dashboard(request):
#     user = request.user
#     designer = Designer.objects.get(user=user)
#     return render(request, "designerViewProducts.html", {'designer': designer})

from .forms import DesignerProfileForm

def designer_dashboard(request):
    user = request.user
    designer = Designer.objects.get(user=user)
    if request.method == 'POST':
        form = DesignerProfileForm(request.POST, request.FILES, instance=designer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
    else:
        form = DesignerProfileForm(instance=designer)
    return render(request, 'designerViewProducts.html', {'form': form})


# add product view
def add_product_view(request):
    return render(request,'addPrd.html',{})

# delete product view
def delete_product_view(request):
    return render(request,'delete_product.html',{})

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
            product.category1 = form.cleaned_data['category1']
            product.category2 = form.cleaned_data['category2']
            product.save()
            form.save_m2m()
            print(request.POST)
            messages.success(request, 'Product added successfully.')
            return redirect('designer_dashboard')
    else:
        form = ProductForm() 

    return render(request, 'addPrd.html', {'form': form})


# =============================================================================================
# view products
# --------------------

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required
def designer_profile(request):
    designer = request.user.designer  # get the designer object of the logged-in user
    products = Product.objects.filter(designer=designer)  # get all products with the designer object
    context = {'designer': designer, 'products': products}
    return render(request, 'designerViewProducts.html', context)


# ==================================================================================================
# edit designer profile
# ===========================


def edit_designer_profile(request):
    designer = Designer.objects.get(user=request.user)
    # designer = request.user.designer # retrieve the designer object
    if request.method == 'POST':
        print(request.POST)
        form = DesignerProfileForm(request.POST, request.FILES, instance=designer)
        if form.is_valid():
            form.save() # save the updated form data to the designer object
            return redirect('designer_dashboard') # redirect to the designer's profile page
    else:
        form = DesignerProfileForm(instance=designer) # pre-populate the form with the current designer's information
    return render(request, 'editInfo.html', {'form': form})


# =======================================================================================================
# product delete
# =====================

# from django.shortcuts import get_object_or_404, redirect

# def delete_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('delete_product_view')
#     return render(request, 'delete_product.html', {'product': product})

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('designer_dashboard')
    return render(request, 'delete_product.html', {'product': product})


# ====================================================================================================
# update stock
# ============================

def update_stock(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock updated successfully.')
            return redirect('designer_dashboard')
        else:
            messages.error(request, 'Error updating stock.')
    else:
        form = StockForm(instance=product)

    context = {'product': product, 'form': form}
    return render(request, 'stockMan.html', context)

# ---------------------------------------------------------------------------------------------------

# designer order status

from django.shortcuts import render, redirect
from customers.models import Order

@login_required
def designer_orders(request):
    designer = get_object_or_404(Designer, user=request.user)
    context = {'designer': designer}
    return render(request, 'designer_order.html', context)

# @login_required
# def change_order_status(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     if order.designer.user != request.user:
#         return redirect('home')
#     if order.status == 'pending':
#         order.status = 'done'
#         order.save()
#     return redirect('designer_order')

@login_required
def change_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.designer.user != request.user:
        return redirect('home')
    if order.status == 'pending':
        order.status = 'done'
        order.save()
        product = order.product
        product_name = product.prd_name
        product.small += order.product.small
        product.medium += order.product.medium
        product.large += order.product.large
        product.extra_large += order.product.extra_large
        product.save()
        messages.success(request, f"The order for {product_name} has been shipped.")
    return redirect('designer_orders')




# designer business
@login_required
def designer_business(request, designer_id):
    designer_business = Order.objects.filter(designer_id=designer_id, status='done')
    context = {'orders': designer_business}
    return render(request, 'designer_business.html', context)


