from django.contrib import admin
from apps.category.models import Category


# Register your models here.
@admin.register(Category)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']
