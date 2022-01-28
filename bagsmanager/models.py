from django.db import models

class Item(models.Model):
    name = models.CharField("Nome", max_length=255)
    value = models.DecimalField("Valor", decimal_places=2, max_digits=8)
    quantity = models.IntegerField("Quantidade")

