from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    records = Record.objects.all()
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
        return render(request, 'home.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "salio exitosamente de la session")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Se a registrado Satisfactoriamente")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        #look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "you Must be Logged In To View That Page..")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Elemento a sido borrado con exito")
        return redirect('home')
    else:
        messages.success(request, "Debes estar logueado para realizar esta accion")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added......")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "Record Added......")
        return redirect('home')




def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "Record Updated......")
        return redirect('home')




