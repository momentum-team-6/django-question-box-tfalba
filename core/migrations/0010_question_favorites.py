# Generated by Django 3.1.5 on 2021-01-09 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='favorites',
            field=models.ManyToManyField(to='core.Favorite'),
        ),
    ]
