# Generated by Django 3.1.5 on 2021-01-09 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210109_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='favorites',
        ),
        migrations.AddField(
            model_name='favorite',
            name='question',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='core.question'),
            preserve_default=False,
        ),
    ]
