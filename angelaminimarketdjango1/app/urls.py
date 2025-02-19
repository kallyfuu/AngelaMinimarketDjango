from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('contacto/',contacto,name="contacto"),
    path('reservapan/',reservapan,name="reservapan"),
    path('agregar-producto/',agregar_producto,name="agregar_producto"),
    path('listar-producto/',listar_producto,name="listar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/',eliminar_producto,name="eliminar_producto"),
    path('registro/',registro,name="registro"),
    path('account/logout/', custom_logout_view, name='logout'),
]
