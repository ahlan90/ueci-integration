# Generated by Django 3.0.7 on 2020-06-24 13:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reluci', '0038_auto_20200624_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observacaotarefaatividade',
            name='observacao',
            field=ckeditor.fields.RichTextField(verbose_name='Observações'),
        ),
    ]