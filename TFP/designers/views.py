from pyexpat.errors import messages
from django.shortcuts import render, redirect


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
def designer_registration(request):
    return render(request,'DesigReg.html',{})

# edit basic info of designer(dp and logo)
def edit_info(request):
    return render(request,'editInfo.html',{})



# ---------------------------------------------------------------------------

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, DesignerRegistrationForm

# def user_registration_view(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(email=email, password=raw_password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'registration/user_registration.html', {'form': form})

# def user_login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid email or password')
#     return render(request, 'registration/user_login.html')
    
def designer_registration_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = DesignerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = DesignerRegistrationForm()
    return render(request, 'desigReg.html', {'form': form})


def designer_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'registration/designer_login.html')
