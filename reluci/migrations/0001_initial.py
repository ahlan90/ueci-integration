# Generated by Django 3.0.6 on 2020-06-02 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoPontoControle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=300)),
                ('descricao', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PontoControle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=300)),
                ('descricao', models.CharField(blank=True, max_length=1000, null=True)),
                ('classificacao', models.CharField(choices=[('ATENDE', 'Atende'), ('ATENDE_PARCIALMENTE', 'Atende parcialmente'), ('NAO_ATENDE', 'Não atende')], max_length=30)),
                ('status', models.CharField(choices=[('NAO_INICIADO', 'Não iniciado'), ('EM_ANDAMENTO', 'Em andamento'), ('FINALIZADO', 'Finalizado')], default='NAO_INICIADO', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=300)),
                ('descricao', models.CharField(blank=True, max_length=1000, null=True)),
                ('ponto_controle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reluci.PontoControle')),
            ],
        ),
    ]
