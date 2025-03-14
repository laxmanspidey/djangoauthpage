from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=150)
    des=models.TextField()
    qty=models.IntegerField()
    price=models.IntegerField()

  
