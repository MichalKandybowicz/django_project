from django.db import models

# Create your models here.


class Products(models.Model):
    # https://docs.djangoproject.com/en/2.1/ref/models/fields/#decimalfield
    # fields information
    name = models.CharField(max_length=40)
    description = models.TextField(default="nice item")
    price = models.DecimalField(max_digits=5000, decimal_places=2)  # now max is 4999,99