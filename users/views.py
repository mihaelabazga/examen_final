
# Create your views here.
from django.shortcuts import render
from .models import Users
def home(request):
    return render(request, "users/home.html",{'message':'Hi, there!'})
def user_detail(request):
    id=Users.id
    user = Users.objects.get(pk=int(id))
    print(user.id)
    context = {
        'users': user,
    }
    return render(request, 'users.html', context)