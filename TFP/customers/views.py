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

# customer - history
# def history(request):
#     return render(request,'history.html',{})

# user profile
def user_profile(request):
    user = request.user
    customer = CustomerProfile.objects.get(user=user)
    return render(request, "userprofile.html", {'customer': customer})

# ==================================================================================================
# edit customer profile
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
    return render(request, 'menbottom.html', {'products': products})

# Women's Fusion Wear
def women_fusion(request):
    products = Product.objects.filter(category1="Women's Fusion Wear")
    return render(request, 'fusion.html', {'products': products})

# Women's Ethnic Wear
def women_ethnic(request):
    products = Product.objects.filter(category1="Women's Ethnic Wear")
    return render(request, 'ethnic.html', {'products': products})


# =======================================================================================================
# product detail

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'user3.html', {'product': product})

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     designer = product.designer
#     return render(request, 'user3.html', {'product': product, 'designer': designer})

from django.db.models import Q

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    designer = product.designer
    reviews = Order.objects.filter(Q(product=product) & ~Q(review='none'))
    return render(request, 'user3.html', {'product': product, 'designer': designer, 'reviews': reviews})



# =============================================================================================================
# designer profile view

def designer_profile(request, pk):
    designer = get_object_or_404(Designer, pk=pk)
    return render(request, 'designerView.html', {'designer': designer})


# =================================================================================================================
# whish list

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

# def cart(request):
#     return render(request,'cart.html')

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product

def cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    customer = CustomerProfile.objects.get(user=request.user)
    designer = product.designer
    context = {'product': product, 'customer': customer, 'designer': designer}
    return render(request, 'cart.html', context)


# --------------------------------------------------------------------------------------------------------------
# order
# ------------------

# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from .models import Order

# def create_order(request, product_id):
#     if request.method == 'POST':
#         customer = request.user
#         product = get_object_or_404(Product, pk=product_id)
#         designer = product.designer
#         size = request.POST.get('size')
#         quantity = int(request.POST.get('quantity'))
#         price = float(request.POST.get('price'))
#         total = float(price) * int(quantity)
#         from_address = designer.email
#         to_address = customer.email
#         status = 'pending'

#         order = Order(customer=customer, product=product, designer=designer, size=size, quantity=quantity, price=price,
#                       total=total, from_address=from_address, to_address=to_address, status=status)
#         order.save()        

#         messages.success(request, 'Your order has been placed!')
#         return redirect('orders_view')

#     product = get_object_or_404(Product, pk=product_id)
#     context = {
#         'product': product
#     }
#     return render(request, 'cart.html', context)


def create_order(request, product_id):
    if request.method == 'POST':
        customer = request.user
        product = get_object_or_404(Product, pk=product_id)
        designer = product.designer
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity'))
        price = float(request.POST.get('price'))
        
        # Check if requested quantity is available for the selected size
        if size == 'small' and quantity > product.small:
            messages.error(request, 'Sorry..! Product is not available in the requested quantity.')
            return redirect('cart', product_id=product_id)
        elif size == 'medium' and quantity > product.medium:
            messages.error(request, 'Sorry..! Product is not available in the requested quantity.')
            return redirect('cart', product_id=product_id)
        elif size == 'large' and quantity > product.large:
            messages.error(request, 'Sorry..! Product is not available in the requested quantity.')
            return redirect('cart', product_id=product_id)
        elif size == 'extra_large' and quantity > product.extra_large:
            messages.error(request, 'Sorry..! Product is not available in the requested quantity.')
            return redirect('cart', product_id=product_id)
        
        # Calculate total price
        total = float(price) * int(quantity)
        
        # Update product stock
        if size == 'small':
            product.small -= quantity
        elif size == 'medium':
            product.medium -= quantity
        elif size == 'large':
            product.large -= quantity
        elif size == 'extra_Large':
            product.extra_large -= quantity
        product.save()
        
        # Create order
        from_address = designer.email
        to_address = customer.email
        status = 'pending'

        order = Order(customer=customer, product=product, designer=designer, size=size, quantity=quantity, price=price,
                      total=total, from_address=from_address, to_address=to_address, status=status)
        order.save()

        messages.success(request, 'Your order has been placed!')
        return redirect('orders_view')

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'cart.html', context)


# ---------------------------------------------------------------------------------------------------------------

# pending orders / your orders

# from django.shortcuts import render
# from .models import Order

# def orders_view(request):
#     orders = Order.objects.all()
#     print(len(orders))
#     context = {'orders': orders}
#     return render(request, 'order.html', context)

from django.shortcuts import render
from .models import Order

def orders_view(request):
    # Filter orders by the logged-in user and status="pending"
    user = request.user
    customer = CustomerProfile.objects.get(user=user)
    orders = Order.objects.filter(customer=request.user, status="pending")

    # Create a context dictionary to pass data to the template
    context = {'orders': orders, 'customer': customer}

    # Render the template with the context data
    return render(request, 'order.html', context)


# ================================================================================

@login_required
def history(request):
    user = request.user
    customer = CustomerProfile.objects.get(user=user)
    orders = Order.objects.filter(customer=user, status='done')
    context = {'orders': orders,  'customer': customer}
    return render(request, 'history.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order

def submit_review(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user, status='done')
    if request.method == 'POST':
        review = request.POST.get('review')
        if review:
            order.review = review
            order.save()
            messages.success(request, 'Your review has been submitted successfully.')
        else:
            messages.error(request, 'Please enter a valid review.')
        return redirect('history')
    else:
        return render(request, 'submit_review.html', {'order': order})
