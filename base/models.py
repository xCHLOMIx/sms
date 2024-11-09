from django.db import models

# Create your models here.

class Product(models.Model):
    code = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name