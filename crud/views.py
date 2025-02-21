from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Render pages
def index(request):
    return render(request, 'crud/form.html')
def deleteForm(request):
    return render(request, 'crud/delete.html')

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

#Delete
def delete(request):
    id = request.POST.get('id')
    if not id:
        messages.error(request, 'ID do usuário não fornecido.')
        return redirect('deleteForm')
    else:
        user = User.objects.filter(id=id).first()
        if user:
            user.delete()
            messages.success(request, 'Usuário deletado com sucesso!')
            return redirect('list_users')
        else:
            messages.error(request, 'Usuário não existe')
            return redirect('deleteForm')