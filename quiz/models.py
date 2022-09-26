from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Questions(models.Model):


    SCALE = (
        ("Fundamental", _("Fundamental")),
        ("Beginner", _("Beginner")),
        ("Intermediate", _("Intermediate")),
        ("Advanced", _("Advanced")),
        ("Expert", _("Expert")),
    )

    TYPE = (
        ("Multiple Choice", _("Multiple Choice")),
        ("True or False", _("True or False")),
        ("Fill the Gap", _("Fill the Gap")),
    )

    subject = models.CharField(max_length=255, default=_(
        "Enter the Quiz Subject"))

    topic = models.CharField(max_length=255, default=_(
        "Enter the Quiz Topic"), verbose_name=_("Quiz Topic"))

    technique = models.CharField(
        choices=TYPE, max_length=15, default="Multiple Choice", verbose_name=_("Type of Question"))

    difficulty = models.CharField(
        choices=SCALE,  max_length=15, default='Fundamental',verbose_name=_("Difficulty"))

    question = models.CharField(max_length=255, verbose_name=_("Question"))

    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))

    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['-date_created']

    def __str__(self):
        return self.question


class Answer(models.Model):

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question_number = models.ForeignKey(
        Questions, related_name='answer', on_delete=models.DO_NOTHING)

    answer_text = models.CharField(
        max_length=255, verbose_name=_("Answer Text"))
        
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
