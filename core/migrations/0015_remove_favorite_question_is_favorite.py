# Generated by Django 3.1.5 on 2021-01-09 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210109_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='question_is_favorite',
        ),
    ]