# Generated by Django 3.1.5 on 2021-01-09 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_favorite_question_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='question_is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]