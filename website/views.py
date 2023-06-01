from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, DbResource
from .models import Record ,articul
from tablib import Dataset


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

def importar(request):
   articuls = articul.objects.all()
   #template = loader.get_template('importar.html')
   if request.method == 'POST':
     db_resource = DbResource()
     dataset = Dataset()
     print(dataset)
     nuevos_articulos = request.FILES['xlsfile']
     print(nuevos_articulos)
     imported_data = dataset.load(nuevos_articulos.read())
     print(dataset)
     result = db_resource.import_data(dataset, dry_run=True) # Test the data import
     print(result.has_errors())
     if not result.has_errors():
       db_resource.import_data(dataset, dry_run=False) # Actually import now
   return render(request, 'importar.html', {'articuls':articuls})




