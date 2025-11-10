# app_Ford/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ==========================================
    # URLS PRINCIPALES
    # ==========================================
    path('', views.inicio_ford, name='inicio'),

    # ==========================================
    # URLS CRUD DE VEHÍCULO
    # ==========================================
    path('vehiculos/agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('vehiculos/ver/', views.ver_vehiculos, name='ver_vehiculos'),
    path('vehiculos/actualizar/<int:id>/', views.actualizar_vehiculo, name='actualizar_vehiculo'),
    path('vehiculos/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_vehiculo, name='realizar_actualizacion_vehiculo'),
    path('vehiculos/borrar/<int:id>/', views.borrar_vehiculo, name='borrar_vehiculo'),

    # ==========================================
    # URLS CRUD DE EMPLEADO
    # ==========================================
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/ver/', views.ver_empleados, name='ver_empleados'),
    path('empleados/actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleados/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),

    # ==========================================
    # URLS CRUD DE VENTA
    # ==========================================
    path('ventas/registrar/', views.agregar_venta, name='agregar_venta'),
    path('ventas/ver/', views.ver_ventas, name='ver_ventas'), # <-- Aquí estaba el error (corregido)
    path('ventas/actualizar/<int:id>/', views.actualizar_venta, name='actualizar_venta'),
    path('ventas/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_venta, name='realizar_actualizacion_venta'),
    path('ventas/borrar/<int:id>/', views.borrar_venta, name='borrar_venta'),
]