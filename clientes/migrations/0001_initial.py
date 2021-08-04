# Generated by Django 3.2.6 on 2021-08-04 16:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idcliente', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idcliente')),
                ('nomecliente', models.CharField(max_length=255)),
                ('razaosocial', models.CharField(max_length=255)),
                ('cpfoucnpj', models.CharField(max_length=20)),
                ('rg', models.CharField(max_length=20)),
                ('ie', models.CharField(max_length=20)),
                ('site', models.CharField(max_length=255)),
                ('apelido', models.CharField(max_length=100)),
                ('idGrupo', models.CharField(max_length=255)),
                ('idGrupoTelemetria', models.CharField(max_length=255)),
                ('informaVelocidade', models.CharField(default='N', max_length=1)),
                ('informaRPM', models.CharField(default='N', max_length=1)),
                ('criadopor', models.CharField(max_length=100)),
                ('editadopor', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
