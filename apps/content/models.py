from django.db import models

from apps.category.models import Category


# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=100)

    # Relationship
    categories = models.ManyToManyField(Category, related_name='subjects')

    class Meta:
        db_table = 'subject'  # <-- Custom table name
        verbose_name = "Subject"
        verbose_name_plural = "All Subjects"

    def __str__(self):
        return self.title


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    # relationship
    subject = models.ForeignKey(Subject,
                                on_delete=models.CASCADE, related_name='topics')  # Use default in case table already having to prevent migration error due foreign key constraint

    class Meta:
        db_table = 'topic'  # <-- Custom table name
        verbose_name = "Topic"
        verbose_name_plural = "All Topics"

    def __str__(self):
        return self.name
