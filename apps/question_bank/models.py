from django.db import models

from apps.content.models import Subject, Topic


# Create your models here.
class LevelOption(models.TextChoices):
    Easy = 'easy', 'Easy'
    Medium = 'medium', 'Medium'
    Hard = 'hard', 'Hard'


class CorrectOption(models.TextChoices):
    A = 'A', 'Option A'
    B = 'B', 'Option B'
    C = 'C', 'Option C'
    D = 'D', 'Option D'


class QuestionPool(models.Model):
    question = models.CharField(max_length=500)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)

    difficulty = models.CharField(max_length=6, choices=LevelOption.choices, default=LevelOption.Easy)
    correct_option = models.CharField(max_length=1, choices=CorrectOption.choices, default=CorrectOption.A, )

    # Relationship
    subject = models.ForeignKey(Subject,
                                on_delete=models.CASCADE,
                                related_name='subjects')  # Use default in case table already having to prevent migration error due foreign key constraint

    topic = models.ForeignKey(Topic,
                              on_delete=models.CASCADE,
                              related_name='topics')  # Use default in case table already having to prevent migration error due foreign key constraint

    class Meta:
        db_table = 'question_pool'  # <-- Custom table name
        verbose_name = "MCQ"
        verbose_name_plural = "All MCQs"

    def __str__(self):
        return self.question
