# Generated by Django 3.0.7 on 2020-06-24 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reluci', '0042_auto_20200624_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='analisepontocontrole',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='observacaotarefaatividade',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
