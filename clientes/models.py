from django.db import models
from django.utils.timezone import now

class Cliente(models.Model):
    idcliente = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idcliente')
    nomecliente = models.CharField(max_length=255)
    razaosocial = models.CharField(max_length=255)
    cpfoucnpj = models.CharField(max_length=20)
    rg = models.CharField(max_length=20, blank=True, null=True)
    ie = models.CharField(max_length=20, blank=True, null=True)
    site = models.CharField(max_length=255, blank=True, null=True)
    apelido = models.CharField(max_length=100, blank=True, null=True)
    idGrupo = models.CharField(max_length=255, blank=True, null=True) 
    idGrupoTelemetria = models.CharField(max_length=255, blank=True, null=True) 
    informaVelocidade = models.CharField(max_length=1, default='N')
    informaRPM = models.CharField(max_length=1, default='N')
    criadopor = models.CharField(max_length=100)
    editadopor = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)
