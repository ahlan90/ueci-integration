# Generated by Django 3.0.6 on 2020-06-02 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NotaEmpenho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50)),
                ('data', models.DateField(null=True)),
                ('historico', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NotaLiquidacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50)),
                ('data', models.DateField(null=True)),
                ('historico', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('numero', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadeGestora',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sigefes.Credor')),
                ('processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sigefes.Processo')),
                ('unidade_gestora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sigefes.UnidadeGestora')),
            ],
        ),
        migrations.CreateModel(
            name='DespesaLiquidada',
            fields=[
                ('despesa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sigefes.Despesa')),
                ('valor_liquidado', models.DecimalField(decimal_places=2, max_digits=20)),
                ('nota_liquidacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sigefes.NotaLiquidacao')),
            ],
            bases=('sigefes.despesa',),
        ),
        migrations.CreateModel(
            name='DespesaEmpenhada',
            fields=[
                ('despesa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sigefes.Despesa')),
                ('valor_empenhado', models.DecimalField(decimal_places=2, max_digits=20)),
                ('nota_empenho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sigefes.NotaEmpenho')),
            ],
            bases=('sigefes.despesa',),
        ),
    ]
