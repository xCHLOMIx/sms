from django.db import models

# Create your models here.

class Product(models.Model):
    code = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name

class ProductIn(models.Model):
    code = models.OneToOneField("base.Product", on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now=False, auto_now_add=True)
    quantity = models.IntegerField()
    unitPrice = models.IntegerField()
    totalPrice = models.IntegerField()

    def __str__(self):
        return self.code.name
    
class ProductOut(models.Model):
    code = models.OneToOneField("base.Product", on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now=False, auto_now_add=True)
    quantity = models.IntegerField()
    unitPrice = models.IntegerField()
    totalPrice = models.IntegerField()

    def __str__(self):
        return self.code.name
    