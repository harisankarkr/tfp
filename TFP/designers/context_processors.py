# from account.models import Designer

# def designer_context_processor(request):
#     designer = None
#     if request.user.is_authenticated:
#         designer = Designer.objects.get(user=request.user)
#     return {'designer': designer}

from django.contrib.auth.models import AnonymousUser
from account.models import Designer

def designer_context_processor(request):
    designer = None
    if request.user.is_authenticated:
        try:
            designer = Designer.objects.get(user=request.user)
        except Designer.DoesNotExist:
            pass
    return {'designer': designer}
