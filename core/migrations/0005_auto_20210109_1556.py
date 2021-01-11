# Generated by Django 3.1.5 on 2021-01-09 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210108_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='core.user'),
            preserve_default=False,
        ),
    ]
