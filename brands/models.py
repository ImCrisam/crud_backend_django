from django.db import models


class Brand(models.Model):
    name = models.CharField("Marca", max_length=100, unique=True)
    owner = models.CharField("Titular", max_length=100, default="desconocido")  # titular de la marca
    is_active = models.BooleanField("Estado", default=True)  # para borrado lógico
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
