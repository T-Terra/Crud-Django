from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def index(request):
    return render(request, 'crud/form.html')

#Create
def users(request):
    new_user = User()
    new_user.name = request.POST.get('nome')
    new_user.age = request.POST.get('idade')
    new_user.save()

    return redirect('list_users')

#Read
def listUsers(request):
    users_db = {
    'users': User.objects.all()
    }
    return render(request, 'crud/users.html', users_db)