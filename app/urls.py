from django.urls import path
from .views import home, menu, agregar, modificar_menu, eliminar_menu

urlpatterns = [
    path('', home, name="home"),
    path('menu/',menu, name="menu"),
    path('agregar-menu/',agregar,name="agregar_menu"),
    path('modificar-menu/<id>/',modificar_menu, name="modificar_menu"),
    path('eliminar-menu/<id>/', eliminar_menu, name="eliminar_menu")
]