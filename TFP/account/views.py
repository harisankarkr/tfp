from django.shortcuts import render,redirect
from django.contrib import messages
from account.forms import UserRegistrationForm
from account.models import Designer,CustomerProfile
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserLoginForm



# ===========================================================================================
# registration
# ==================

def registration(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_designer = form.cleaned_data['is_designer']
            user.save()

            if user.is_designer:
                Designer.objects.create(
                    user=user, 
                    name=user.username,
                    email=user.email, 
                    phone=user.mobile
                )
            else:
                CustomerProfile.objects.create(
                    user=user, 
                    name=user.username,
                    email=user.email, 
                    phone=user.mobile
                )

            messages.success(request, f'Account created for {user.username}!')
            return redirect('index')
        else:
            # display form validation errors
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()

    return render(request, 'index.html', {'form': form})


# ===========================================================================================
# login
# ==================


def user_login(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                if user.is_designer:
                    return redirect('designer_dashboard')
                else:
                    return redirect('customer_dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()

    return render(request, 'index.html', {'form': form})


# ===========================================================================================

# logout
# =========================

def logout_view(request):
    logout(request)
    return redirect('index')

# =============================================================================================

# index | login view
# ==========================
def index_login_view(request):
    return render(request,"index.html",{})

