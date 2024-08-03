from django.db import models # type: ignore

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Enter description here.")

    def __str__(self):
        return self.name

class GroceryItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name
