# Generated by Django 3.0.7 on 2020-06-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reluci', '0032_itemgestao_percentual'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analisepontocontrole',
            options={'ordering': ('-criado',)},
        ),
        migrations.AlterField(
            model_name='analisepontocontrole',
            name='classificacao',
            field=models.CharField(choices=[('NAO_AVALIADO', 'Não avaliado'), ('ATENDE', 'Atende'), ('ATENDE_PARCIALMENTE', 'Atende parcialmente'), ('NAO_ATENDE', 'Não atende')], default='NAO_AVALIADO', max_length=30),
        ),
        migrations.AlterField(
            model_name='analisesubpontocontrole',
            name='classificacao',
            field=models.CharField(choices=[('NAO_AVALIADO', 'Não avaliado'), ('ATENDE', 'Atende'), ('ATENDE_PARCIALMENTE', 'Atende parcialmente'), ('NAO_ATENDE', 'Não atende')], default='NAO_AVALIADO', max_length=30),
        ),
    ]