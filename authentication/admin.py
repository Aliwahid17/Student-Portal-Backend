from django.contrib import admin
from authentication import models

# Register your models here.

@admin.register(models.User)
class Users(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'username',
        # 'password1',
        # 'password2',
        'phone',
        # 'address',
        'date_created'
    ]