# Generated by Django 3.1.5 on 2021-01-10 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210110_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='has_correct_answer',
        ),
    ]