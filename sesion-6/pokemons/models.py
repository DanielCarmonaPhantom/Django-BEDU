from django.db import models

# Create your models here.


class Type(models.Model):
    name = models.CharField(max=255)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_lenght=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
