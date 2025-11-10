# app_Ford/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo, Empleado, Venta
from datetime import date 

# ==========================================
# VISTAS PRINCIPALES
# ==========================================

def inicio_ford(request):
    """
    Renderiza la página de inicio.
    """
    return render(request, 'inicio.html')

# ==========================================
# VISTAS CRUD DE VEHÍCULO (CORREGIDAS)
# ==========================================

def agregar_vehiculo(request):
    if request.method == "POST":
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        anio = request.POST.get('anio')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad_disponible')
        
        # --- CAMPOS CORREGIDOS ---
        numero_serie = request.POST.get('numero_serie')
        color = request.POST.get('color')

        Vehiculo.objects.create(
            marca=marca,
            modelo=modelo,
            anio=anio,
            precio=precio,
            cantidad_disponible=cantidad,
            # --- CAMPOS AÑADIDOS ---
            numero_serie=numero_serie,
            color=color
        )
        return redirect('ver_vehiculos') 
    
    return render(request, 'vehiculos/agregar_vehiculo.html')


def ver_vehiculos(request):
    todos_los_vehiculos = Vehiculo.objects.all()
    contexto = {
        'vehiculos': todos_los_vehiculos
    }
    return render(request, 'vehiculos/ver_vehiculos.html', contexto)


def actualizar_vehiculo(request, id):
    vehiculo_a_actualizar = get_object_or_404(Vehiculo, id=id)
    contexto = {
        'vehiculo': vehiculo_a_actualizar
    }
    return render(request, 'vehiculos/actualizar_vehiculo.html', contexto)


def realizar_actualizacion_vehiculo(request, id):
    vehiculo_a_actualizar = get_object_or_404(Vehiculo, id=id)
    
    if request.method == "POST":
        vehiculo_a_actualizar.marca = request.POST.get('marca')
        vehiculo_a_actualizar.modelo = request.POST.get('modelo')
        vehiculo_a_actualizar.anio = request.POST.get('anio')
        vehiculo_a_actualizar.precio = request.POST.get('precio')
        vehiculo_a_actualizar.cantidad_disponible = request.POST.get('cantidad_disponible')
        
        # --- CAMPOS CORREGIDOS ---
        vehiculo_a_actualizar.numero_serie = request.POST.get('numero_serie')
        vehiculo_a_actualizar.color = request.POST.get('color')
        
        vehiculo_a_actualizar.save()
        return redirect('ver_vehiculos')
    
    return redirect('ver_vehiculos')


def borrar_vehiculo(request, id):
    vehiculo_a_borrar = get_object_or_404(Vehiculo, id=id)
    vehiculo_a_borrar.delete()
    
    return redirect('ver_vehiculos')

# ==========================================
# VISTAS CRUD DE EMPLEADO (Estaban correctas)
# ==========================================

def agregar_empleado(request):
    """
    Vista para registrar un nuevo empleado.
    Maneja GET (mostrar formulario) y POST (guardar datos).
    """
    if request.method == "POST":
        # Extraer datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        puesto = request.POST.get('puesto')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        fecha_contratacion = request.POST.get('fecha_contratacion')
        salario = request.POST.get('salario')

        # Manejar valores opcionales que pueden venir vacíos
        if not fecha_contratacion:
            fecha_contratacion = None
        
        if not salario:
            salario = None

        # Crear y guardar el nuevo empleado
        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            puesto=puesto,
            telefono=telefono,
            email=email,
            fecha_contratacion=fecha_contratacion,
            salario=salario
        )
        return redirect('ver_empleados') # Redirigir a la lista de empleados

    # Si es GET, solo mostrar el formulario
    return render(request, 'empleados/agregar_empleado.html')

def ver_empleados(request):
    """
    Muestra una lista de todos los empleados en la base de datos.
    """
    todos_los_empleados = Empleado.objects.all()
    contexto = {
        'empleados': todos_los_empleados
    }
    return render(request, 'empleados/ver_empleados.html', contexto)

def actualizar_empleado(request, id):
    """
    Muestra el formulario con los datos actuales del empleado para editar.
    """
    empleado_a_actualizar = get_object_or_404(Empleado, id=id)
    contexto = {
        'empleado': empleado_a_actualizar
    }
    return render(request, 'empleados/actualizar_empleado.html', contexto)

def realizar_actualizacion_empleado(request, id):
    """
    Procesa los datos enviados desde el formulario de actualización de empleado.
    """
    empleado_a_actualizar = get_object_or_404(Empleado, id=id)
    
    if request.method == "POST":
        empleado_a_actualizar.nombre = request.POST.get('nombre')
        empleado_a_actualizar.apellido = request.POST.get('apellido')
        empleado_a_actualizar.puesto = request.POST.get('puesto')
        empleado_a_actualizar.telefono = request.POST.get('telefono')
        empleado_a_actualizar.email = request.POST.get('email')
        
        fecha_contratacion = request.POST.get('fecha_contratacion')
        empleado_a_actualizar.fecha_contratacion = fecha_contratacion if fecha_contratacion else None
        
        salario = request.POST.get('salario')
        empleado_a_actualizar.salario = salario if salario else None

        empleado_a_actualizar.save()
        return redirect('ver_empleados')
    
    return redirect('ver_empleados')

def borrar_empleado(request, id):
    """
    Elimina un empleado de la base de datos.
    """
    empleado_a_borrar = get_object_or_404(Empleado, id=id)
    empleado_a_borrar.delete()
    return redirect('ver_empleados')


# ==========================================
# VISTAS CRUD DE VENTA (Estaban correctas)
# ==========================================

def agregar_venta(request):
    vehiculos = Vehiculo.objects.all() 
    empleados = Empleado.objects.all() 

    if request.method == "POST":
        vehiculo_id = request.POST.get('vehiculo')
        empleado_id = request.POST.get('empleado')
        cliente_nombre = request.POST.get('cliente_nombre')
        cliente_telefono = request.POST.get('cliente_telefono')
        total = request.POST.get('total')
        metodo_pago = request.POST.get('metodo_pago')
        folio = request.POST.get('folio')

        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        empleado = get_object_or_404(Empleado, id=empleado_id) if empleado_id else None 

        Venta.objects.create(
            vehiculo=vehiculo,
            empleado=empleado,
            cliente_nombre=cliente_nombre,
            cliente_telefono=cliente_telefono,
            total=total,
            metodo_pago=metodo_pago,
            folio=folio,
            fecha_venta=date.today() 
        )
        
        if vehiculo.cantidad_disponible > 0:
             vehiculo.cantidad_disponible -= 1
             vehiculo.save()

        return redirect('ver_ventas')
    
    contexto = {
        'vehiculos': vehiculos,
        'empleados': empleados
    }
    return render(request, 'ventas/agregar_venta.html', contexto)


def ver_ventas(request):
    todas_las_ventas = Venta.objects.select_related('vehiculo', 'empleado').all()
    contexto = {
        'ventas': todas_las_ventas
    }
    return render(request, 'ventas/ver_ventas.html', contexto)


def actualizar_venta(request, id):
    venta_a_actualizar = get_object_or_404(Venta, id=id)
    vehiculos = Vehiculo.objects.all()
    empleados = Empleado.objects.all()

    contexto = {
        'venta': venta_a_actualizar,
        'vehiculos': vehiculos,
        'empleados': empleados
    }
    return render(request, 'ventas/actualizar_venta.html', contexto)


def realizar_actualizacion_venta(request, id):
    venta_a_actualizar = get_object_or_404(Venta, id=id)
    
    if request.method == "POST":
        vehiculo_anterior = venta_a_actualizar.vehiculo
        vehiculo_nuevo_id = request.POST.get('vehiculo')
        vehiculo_nuevo = get_object_or_404(Vehiculo, id=vehiculo_nuevo_id)

        venta_a_actualizar.vehiculo = vehiculo_nuevo
        venta_a_actualizar.empleado = get_object_or_404(Empleado, id=request.POST.get('empleado')) if request.POST.get('empleado') else None
        venta_a_actualizar.cliente_nombre = request.POST.get('cliente_nombre')
        venta_a_actualizar.cliente_telefono = request.POST.get('cliente_telefono')
        venta_a_actualizar.total = request.POST.get('total')
        venta_a_actualizar.metodo_pago = request.POST.get('metodo_pago')
        venta_a_actualizar.folio = request.POST.get('folio')

        venta_a_actualizar.save()

        if vehiculo_anterior.id != vehiculo_nuevo.id:
            vehiculo_anterior.cantidad_disponible += 1 
            vehiculo_anterior.save()
            if vehiculo_nuevo.cantidad_disponible > 0:
                vehiculo_nuevo.cantidad_disponible -= 1 
                vehiculo_nuevo.save()

        return redirect('ver_ventas')
    
    return redirect('ver_ventas')


def borrar_venta(request, id):
    venta_a_borrar = get_object_or_404(Venta, id=id)
    vehiculo_vendido = venta_a_borrar.vehiculo 

    venta_a_borrar.delete()
    
    vehiculo_vendido.cantidad_disponible += 1
    vehiculo_vendido.save()
    
    return redirect('ver_ventas')