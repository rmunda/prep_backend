from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'  # <-- Custom table name
        verbose_name = "Category"
        verbose_name_plural = "All Categories"

    def __str__(self):
        return self.title
