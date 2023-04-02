from django.shortcuts import render,redirect
from django.contrib import messages
from account.forms import UserRegistrationForm
from account.models import Designer,CustomerProfile
# Create your views here.



# def registration(request):
#     if request.method == 'POST':
#         print(request.POST)
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()

#     return render(request,'index.html',{'form':form})



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
            return redirect('login')
        else:
            # display form validation errors
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()

    return render(request, 'index.html', {'form': form})


# index | login view
def index_login_view(request):
    return render(request,"index.html",{})

