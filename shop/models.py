from django.db import models

# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')