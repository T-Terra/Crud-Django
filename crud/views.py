from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Render pages
def index(request):
    return render(request, 'crud/form.html')
def deleteForm(request):
    return render(request, 'crud/delete.html')
def updateForm(request):
    return render(request, 'crud/updateForm.html')

#Create
def users(request):
    new_user = User()
    name = request.POST.get('nome')
    age = request.POST.get('idade')
    if not name and not age:
        messages.error(request, 'Dados do usuário não fornecido!')
        return redirect('home')
    else:
        new_user.name = name
        new_user.age = age
        new_user.save()
        messages.success(request, 'Usuário Salvo com sucesso!')
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

#Update
def update(request):
    id = request.POST.get('id')
    name = request.POST.get('nome')
    age = request.POST.get('idade')
    if not id and not name and not age:
        messages.error(request, 'Dados do usuário não fornecido!')
        return redirect('updateForm')
    else:
        user = User.objects.filter(id=id).first()
        if user:
            user.name = name
            user.age = age
            user.save()
            messages.success(request, f'Usuário atualizado com sucesso! {id} - {name}')
            return redirect('list_users')