from django.db import models

# Create your models here.
class Creditos(models.Model):
  banco = models.TextField("Banco")
  valor = models.IntegerField("Valor")
  Banco_id = models.TextField("Banco_id")