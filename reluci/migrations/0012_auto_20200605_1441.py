# Generated by Django 3.0.6 on 2020-06-05 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reluci', '0011_delete_itensgestao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='ponto_controle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atividades', to='reluci.PontoControle'),
        ),
    ]
