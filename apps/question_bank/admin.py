from django.contrib import admin
from .models import QuestionPool
from apps.content.models import Subject, Topic


# Register your models here.

class SubjectListFilter(admin.SimpleListFilter):
    title = 'Subject'  # This is the label shown in the sidebar
    parameter_name = 'subject'

    def lookups(self, request, model_admin):
        return [(t.id, t.title) for t in Subject.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(subject__id=self.value())
        return queryset

class TopicListFilter(admin.SimpleListFilter):
    title = 'Topic'  # This is the label shown in the sidebar
    parameter_name = 'topic'

    def lookups(self, request, model_admin):
        return [(t.id, t.name) for t in Topic.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(topic__id=self.value())
        return queryset


@admin.register(QuestionPool)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'correct_option', 'difficulty', 'topic', 'subject')
    search_fields = ['question_text']
    list_filter = ('difficulty', SubjectListFilter, TopicListFilter)

    # In case of override[Field->text,correct_option]
    # list_display_links = ('question_text', 'answer_text')  # This makes it blue (clickable)[Applies to row data]

    # def question_text(self, obj):
    #     return obj.question
    #
    # question_text.short_description = 'Question'  # <-- This renames the column header
    #
    # def answer_text(self, obj):
    #     return obj.correct_option
    #
    # answer_text.short_description = 'Answer'  # <-- This renames the column header
