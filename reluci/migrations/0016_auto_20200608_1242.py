# Generated by Django 3.0.6 on 2020-06-08 15:42

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reluci', '0015_auto_20200608_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividade',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='atividade',
            name='ponto_controle',
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('observacao', ckeditor.fields.RichTextField()),
                ('status', models.CharField(choices=[('NAO_INICIADO', 'Não iniciado'), ('EM_ANDAMENTO', 'Em andamento'), ('FINALIZADO', 'Finalizado')], default='NAO_INICIADO', max_length=30)),
                ('ponto_controle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to='reluci.PontoControle')),
            ],
        ),
        migrations.CreateModel(
            name='SubPontoControle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=300)),
                ('descricao', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(choices=[('NAO_INICIADO', 'Não iniciado'), ('EM_ANDAMENTO', 'Em andamento'), ('FINALIZADO', 'Finalizado')], default='NAO_INICIADO', max_length=30)),
                ('observacao', ckeditor.fields.RichTextField()),
                ('ponto_controle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reluci.SubPontoControle')),
            ],
        ),
        migrations.AddField(
            model_name='atividade',
            name='tarefa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='atividades', to='reluci.Tarefa'),
            preserve_default=False,
        ),
    ]