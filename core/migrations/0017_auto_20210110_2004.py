# Generated by Django 3.1.5 on 2021-01-10 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_favorite_question_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='core.question'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='question_is_favorite',
            field=models.BooleanField(default=True),
        ),
    ]