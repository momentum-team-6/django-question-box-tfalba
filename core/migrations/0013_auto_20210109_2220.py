# Generated by Django 3.1.5 on 2021-01-09 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210109_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='users',
        ),
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
        migrations.AddField(
            model_name='favorite',
            name='question_is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='core.user'),
            preserve_default=False,
        ),
    ]