from django.contrib import admin
from quiz import models

# Register your models here.


class Answer(admin.TabularInline):
    model = models.Answer
    fields = [
        'question_number',
        'answer_text',
        'is_right'
    ]


@admin.register(models.Questions)
class Questions(admin.ModelAdmin):
    list_display = [
        'subject',
        'topic',
        'technique',
        'difficulty',
        'question',
        'difficulty',
        'date_created',
        'is_active'
    ]

    inlines = [
        Answer
    ]


