# Generated by Django 3.0.6 on 2020-06-15 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reluci', '0029_auto_20200610_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividade',
            name='observacao',
        ),
    ]
