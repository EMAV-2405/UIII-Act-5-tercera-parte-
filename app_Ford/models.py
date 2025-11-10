# app_Ford/models.py
from django.db import models

# ==========================================
# MODELO: EMPLEADO
# ==========================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_contratacion = models.DateField(blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self):  
        return f"{self.nombre} {self.apellido}"  

# ==========================================
# MODELO: VEHÍCULO
# ==========================================
class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    color = models.CharField(max_length=50, blank=True, null=True)
    numero_serie = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    cantidad_disponible = models.PositiveIntegerField(default=1)
    
    def __str__(self):  
        return f"{self.marca} {self.modelo} ({self.anio})"  

# ==========================================
# MODELO: VENTA
# ==========================================
class Venta(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='ventas')
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True, related_name='ventas')
    cliente_nombre = models.CharField(max_length=150)
    cliente_telefono = models.CharField(max_length=50, blank=True, null=True)
    fecha_venta = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, blank=True, null=True)
    folio = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):  
        return f"Venta {self.folio or self.id}"

