from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from customers.models import Wishlist
from account.models import Designer
from designers.models import Product
from account.models import CustomerProfile
from customers.forms import CustAddressForm


# customer registration page view
def customer_registration(request):
    return render(request,'customerReg.html',{})

# customer base
def userpage1(request):
    return render(request,'user1.html',{})

# customer base
def userpage2(request):
    return render(request,'user2.html',{})

# customer - user page 1
def customer_dashboard(request):
    return render(request,'customer_base.html',{})

# user profile
def user_profile(request):
    user = request.user
    customer = CustomerProfile.objects.get(user=user)
    return render(request, "userprofile.html", {'customer': customer})

# ==================================================================================================
# edit designer profile
# ===========================


def edit_customer_address(request):
    customer = CustomerProfile.objects.get(user=request.user)
    # designer = request.user.designer # retrieve the designer object
    if request.method == 'POST':
        print(request.POST)
        form = CustAddressForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save() # save the updated form data to the designer object
            return redirect('user_profile') # redirect to the designer's profile page
    else:
        form = CustAddressForm(instance=customer) # pre-populate the form with the current designer's information
    return render(request, 'userprofile.html', {'form': form})


# ========================================================================================================
# display all the products

def all_products(request):
    products = Product.objects.all()
    return render(request, 'user2.html', {'products': products})

# def all_products(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         # context = {'products': products}
#         return render(request, 'user2.html', {'products': products})
    
# def all_products(request):
#     if request.method == 'GET':
#         products = Product.objects.select_related("Men's Topwear").all()
#         return render(request, 'user2.html', {'products': products})
    
# =====================================================================================================

# men's topwear
def men_topwear(request):
    products = Product.objects.filter(category1="Men's Topwear")
    return render(request, 'user2.html', {'products': products})

# Men's Bottomwear
def men_bottomwear(request):
    products = Product.objects.filter(category1="Men's Bottomwear")
    return render(request, 'user2.html', {'products': products})

# Women's Fusion Wear
def women_fusion(request):
    products = Product.objects.filter(category1="Women's Fusion Wear")
    return render(request, 'user2.html', {'products': products})

# Women's Ethnic Wear
def women_ethnic(request):
    products = Product.objects.filter(category1="Women's Ethnic Wear")
    return render(request, 'user2.html', {'products': products})


# =======================================================================================================
# product detail

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'user3.html', {'product': product})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    designer = product.designer
    return render(request, 'user3.html', {'product': product, 'designer': designer})


# =============================================================================================================
# designer profile view

def designer_profile(request, pk):
    designer = get_object_or_404(Designer, pk=pk)
    return render(request, 'designerView.html', {'designer': designer})


# =================================================================================================================
# whish list

# def wishlist(request):
#     wishlist = get_object_or_404(Wishlist, user=request.user)
#     products = wishlist.products.all()
#     return render(request, 'wishlist.html', {'products': products})

# def wishlist(request):
#     wishlist = get_object_or_404(Wishlist, user=request.user)
#     products = wishlist.products.all()
#     customer = CustomerProfile.objects.get(user=request.user)
#     context = {
#         'customer': customer,
#         'products': products,
#     }
#     return render(request, 'wishlist.html', context)

def wishlist(request):
    wishlist = get_object_or_404(Wishlist, user=request.user)
    products = wishlist.products.all()
    customer = CustomerProfile.objects.get(user=request.user)
    context = {
        'customer': customer,
        'products': products,
    }
    if not products:
        context['empty_wishlist'] = True
    return render(request, 'wishlist.html', context)


def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    messages.success(request, f"{product.prd_name} has been added to your wishlist.")
    return redirect('wishlist')



def remove_from_wishlist(request, pk):
    product = Product.objects.get(pk=pk)
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.products.remove(product)
    messages.success(request, f"{product.prd_name} has been removed from your wishlist.")
    return redirect('wishlist')

# ==============================================================================================================
# cart
# -----------

def cart(request):
    return render(request,'cart.html')