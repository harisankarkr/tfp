from django.shortcuts import render,redirect
from django.contrib import messages
from account.forms import UserRegistrationForm
# Create your views here.



def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request,'customerReg.html',{'form':form})

# index | login view
def index_login_view(request):
    return render(request,"index.html",{})

