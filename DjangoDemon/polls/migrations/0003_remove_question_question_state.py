# Generated by Django 2.2.5 on 2019-12-28 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_question_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_state',
        ),
    ]
