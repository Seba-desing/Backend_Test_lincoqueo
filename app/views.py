from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu
from .forms import MenuForm

# Create your views here.
def home(request):

    return render(request, "app/home.html")

def menu(request):
    menus = Menu.objects.all
    data = {
        "menus" : menus
    }
    return render(request,"app/menu.html", data)

def agregar(request):
    data = {
        "form": MenuForm()
    }

    if request.method == 'POST':
        formulario = MenuForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Agregado correctamente"
        else:
            data["form"] = formulario    

    return render(request,"app/Menu/agregarmenu.html",data)    

def modificar_menu(request, id):

    menu = get_object_or_404(Menu, id=id)

    data={
        'form': MenuForm(instance=menu)
    }
    if request.method == 'POST':
        formulario = MenuForm(data=request.POST, instance=menu, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="menu")
        data["form"] = formulario    
        
    return render(request,"app/Menu/modificar.html",data)    
def eliminar_menu(request,id):
    menu = get_object_or_404(Menu, id=id)
    menu.delete()

    return redirect(to="menu")