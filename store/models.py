from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    clientes = models.BooleanField(default=True)
    telefono = models.CharField(max_length=11, unique=True)
    address = models.TextField()
    dni = models.CharField(max_length=12, unique=True)


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


class Factura(models.Model):
    numero = models.PositiveIntegerField()
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        cadena = f"{self.numero} - {self.fecha.strftime('%d/%m/%Y')}"
        return cadena

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"


class DetalleFactura(models.Model):
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.cantidad <= 0:
            raise ValidationError("La cantidad debe ser mayor que 0.")

        if self.cantidad > self.id_producto.stock:
            raise ValidationError(
                f"No hay suficiente stock de "
                f"{self.id_producto.nombre}. "
                f"Solo quedan {self.id_producto.stock}"
            )

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)