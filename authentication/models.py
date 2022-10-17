from django.db import models
from authentication.hashers import ParameterCheckers


# Create your models here.


class User(models.Model):

    name = models.CharField(blank=False, max_length=40,
                            editable=True, verbose_name="Name",validators=[ParameterCheckers.validate_name])

    email = models.EmailField(
        unique=True, max_length=40, editable=True, blank=False, verbose_name="Email",validators=[ParameterCheckers.validate_email])

    username = models.CharField(unique=True,blank=False, max_length=25, verbose_name="Username",validators=[ParameterCheckers.validate_username])

    password = models.CharField(
        editable=True, blank=False, max_length=100, verbose_name="Password",validators=[ParameterCheckers.validate_password])

    password2 = models.CharField(
        editable=True, blank=False, max_length=100, verbose_name="Re-Password",validators=[ParameterCheckers.validate_password])

    phone = models.CharField(
        unique=True, editable=True, max_length=15,blank=False, verbose_name="Phone",validators=[ParameterCheckers.validate_phone])

    address = models.CharField(
        max_length=120, editable=True, blank=False, verbose_name="Address")

    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Date Created")


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['-date_created']

    def __str__(self):
        return self.name
