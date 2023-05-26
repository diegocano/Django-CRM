from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #autentificacion
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Ingreso exitoso!")
            return redirect('home')
        else:
            messages.success(request, "Error loguese de nuevo, intente de nuevo")
            return redirect('home')
    else:
        return render(request, 'home.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, "salio exitosamente de la session")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})





