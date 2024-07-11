from django.shortcuts import render,redirect,get_object_or_404
from .models import Panesbd
from .forms import ContactoForms,ProductoForms,CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def contacto(request):
    data = {
        'form': ContactoForms()
    }

    if request.method == 'POST':
        formulario = ContactoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario

    return render(request,'app/contacto.html', data)

def reservapan(request):
    productos = Panesbd.objects.all()
    data = {
        'productos': productos
    }
    return render(request,'app/reservapan.html', data)

@permission_required('app.add_panesbd')
def agregar_producto(request):
    data = {
        'form': ProductoForms
    }
    if request.method == 'POST':
        formulario = ProductoForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto registrado")
        else:
            data["form"] = formulario
    return render(request, 'app/CRUD/agregar.html',data)

@permission_required('app.view_panesbd')
def listar_producto(request):
    productos = Panesbd.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/CRUD/listar.html',data)

@permission_required('app.change_panesbd')
def modificar_producto(request, id):
    producto = get_object_or_404(Panesbd, id=id)
    data = {
        'form': ProductoForms(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForms(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"modificado correctamente")
            return redirect(to="listar_producto")
        data["form"] = formulario

    return render(request, 'app/CRUD/modificar.html',data )

@permission_required('app.delete_panesbd')
def eliminar_producto(request, id):
    producto = get_object_or_404(Panesbd, id=id)
    producto.delete()
    messages.success(request,"eliminado correctamente")
    return redirect(to="listar_producto")

def registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html',data)

def custom_logout_view(request):
    logout(request)
    return redirect('/')