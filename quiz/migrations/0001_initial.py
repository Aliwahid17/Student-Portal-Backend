# Generated by Django 4.1.1 on 2022-09-26 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='Enter the Quiz Subject', max_length=255)),
                ('topic', models.CharField(default='Enter the Quiz Topic', max_length=255, verbose_name='Quiz Topic')),
                ('technique', models.CharField(choices=[('Multiple Choice', 'Multiple Choice'), ('True or False', 'True or False'), ('Fill the Gap', 'Fill the Gap')], default='Multiple Choice', max_length=15, verbose_name='Type of Question')),
                ('difficulty', models.CharField(choices=[('Fundamental', 'Fundamental'), ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Expert', 'Expert')], default='Fundamental', max_length=15, verbose_name='Difficulty')),
                ('question', models.CharField(max_length=255, verbose_name='Question')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active Status')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=255, verbose_name='Answer Text')),
                ('is_right', models.BooleanField(default=False)),
                ('question_number', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer', to='quiz.questions')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'ordering': ['id'],
            },
        ),
    ]