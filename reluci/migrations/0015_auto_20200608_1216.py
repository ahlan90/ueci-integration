# Generated by Django 3.0.6 on 2020-06-08 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reluci', '0014_atividade_observacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pontocontrole',
            old_name='sintese',
            new_name='analise',
        ),
    ]
