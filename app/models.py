from django.db import models

# Create your models here.

class Menu(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.TextField()
    imagen = models.ImageField(upload_to="comida", null=True)

    def __str__(self):
        return self.nombre