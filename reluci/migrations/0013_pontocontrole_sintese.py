# Generated by Django 3.0.6 on 2020-06-05 18:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reluci', '0012_auto_20200605_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontocontrole',
            name='sintese',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]