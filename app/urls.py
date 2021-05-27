from django.urls import path
from .views import home, menu, agregar

urlpatterns = [
    path('', home, name="home"),
    path('menu/',menu, name="menu"),
    path('agregar-menu/',agregar,name="agregar_menu")
]