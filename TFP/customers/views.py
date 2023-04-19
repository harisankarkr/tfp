from django.shortcuts import get_object_or_404, redirect, render
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

# =======================================================================================================
# product detail

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'user3.html', {'product': product})

# =============================================================================================================