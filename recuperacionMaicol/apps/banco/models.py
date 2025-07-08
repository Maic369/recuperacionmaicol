from django.db import models

# Create your models here.
class Banco(models.Model):
  usuario = models.TextField("Usuario")
  transaccion = models.IntegerField("Transaccion")
  rol_id = models.TextField("Rol_id")