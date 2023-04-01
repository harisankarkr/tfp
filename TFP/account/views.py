from django.shortcuts import render

# Create your views here.

# index | login view
def index_login_view(request):
    return render(request,"index.html",{})

