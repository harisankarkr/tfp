
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .forms import DesignerRegistrationForm

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


# designer registraion

def designer_registration(request):
    if request.method == 'POST':
        form = DesignerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('index')
    else:
        form = DesignerRegistrationForm()
    return render(request, 'DesigReg.html', {'form': form})


# designer login

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import DesignerLoginForm

def designer_login(request):
    if request.method == 'POST':
        form = DesignerLoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_designer:
                login(request, user)
                return redirect('base')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = DesignerLoginForm()
    return render(request, 'index.html', {'form': form})

