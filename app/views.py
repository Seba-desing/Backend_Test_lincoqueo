from django.shortcuts import render
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