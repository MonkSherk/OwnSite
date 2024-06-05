from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='store_img%d-%m-%Y')
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_img%d-%m-%Y')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_img%d-%m-%Y')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
