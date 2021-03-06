# Generated by Django 3.0.7 on 2020-06-24 12:57

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reluci', '0036_auto_20200622_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservacaoTarefaAtividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NAO_INICIADO', 'Não iniciado'), ('EM_ANDAMENTO', 'Em andamento'), ('AGUARDANDO', 'Aguardando'), ('FINALIZADO', 'Finalizado')], default='NAO_INICIADO', max_length=30)),
                ('observacao', ckeditor.fields.RichTextField()),
                ('atividade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reluci.Atividade')),
                ('tarefa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reluci.Tarefa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='observacaotarefa',
            name='tarefa',
        ),
        migrations.RemoveField(
            model_name='observacaotarefa',
            name='user',
        ),
        migrations.DeleteModel(
            name='ObservacaoAtividade',
        ),
        migrations.DeleteModel(
            name='ObservacaoTarefa',
        ),
    ]
