# Generated by Django 3.2.6 on 2021-08-07 13:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Naoconformidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoViagem', models.IntegerField()),
                ('DataCadastro', models.DateTimeField(blank=True, null=True)),
                ('Descricao', models.CharField(max_length=255)),
                ('DescricaoTipoNC', models.CharField(max_length=255)),
                ('Placa', models.CharField(max_length=20)),
                ('TipoNC', models.IntegerField()),
                ('data_alteracao', models.DateTimeField(blank=True, null=True)),
                ('idNC', models.IntegerField()),
                ('ornc_data_leitura_gr', models.CharField(max_length=255)),
                ('ornc_data_leitura_site', models.CharField(max_length=255)),
                ('ornc_esis_codigo', models.CharField(max_length=255)),
                ('ornc_usua_pfis_pess_oras_codigo', models.IntegerField()),
                ('usua_login', models.CharField(max_length=255)),
                ('usua_pess_nome', models.CharField(max_length=255)),
                ('informativogrupo', models.CharField(default='N', max_length=1)),
                ('data_hora_integrada', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('data_hora_atualizacao', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]