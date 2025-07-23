from django.contrib import admin
from apps.content.models import Subject, Topic
from apps.category.models import Category


# Register your models here.

class CategoryListFilter(admin.SimpleListFilter):
    title = 'Category'  # This is the label shown in the sidebar
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        return [(t.id, t.title) for t in Category.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category__id=self.value())
        return queryset


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']
    list_filter = (CategoryListFilter,)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject',)
    search_fields = ['name', 'subject__title']
    list_filter = ('name', 'subject__title',)
