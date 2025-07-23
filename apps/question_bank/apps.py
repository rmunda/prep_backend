from django.apps import AppConfig


class QuestionBankConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.question_bank'
    verbose_name = 'Manage MCQs'  # Custom name shown in admin
