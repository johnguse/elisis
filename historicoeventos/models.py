from django.db import models
from django.utils.timezone import now

# Create your models here.
class Historicodeeventos(models.Model):
    id_evento = models.AutoField(primary_key=True)
    tipo_evento = models.IntegerField(blank=True, null=True)
    descricao_tipo_evento = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    placa = models.CharField(max_length=20, blank=True, null=True)
    veic_oras_codigo = models.IntegerField(blank=True, null=True)
    numero_terminal = models.CharField(max_length=255, blank=True, null=True)
    tecnologia = models.CharField(max_length=255, blank=True, null=True)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    data_bordo = models.DateTimeField(blank=True, null=True)
    posicao = models.TextField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    codigo_viagem = models.IntegerField(blank=True, null=True)
    viag_numero_manifesto = models.IntegerField(blank=True, null=True)
    esis_usuario_adicionou = models.CharField(max_length=255, blank=True, null=True)
    pess_nome_adicionou = models.CharField(max_length=255, blank=True, null=True)
    pess_oras_codigo_adicionou = models.IntegerField(blank=True, null=True)
    pess_oras_codigo_leitura = models.IntegerField(blank=True, null=True)
    usua_login_leitura = models.CharField(max_length=255, blank=True, null=True)
    pess_nome_leitura = models.CharField(max_length=255, blank=True, null=True)
    pess_oras_codigo_supervisao = models.IntegerField(blank=True, null=True)
    usua_login_supervisao = models.CharField(max_length=255, blank=True, null=True)
    pess_nome_supervisao = models.CharField(max_length=255, blank=True, null=True)
    esis_data_leitura = models.DateTimeField(blank=True, null=True)
    esis_desc_tratamento = models.TextField(blank=True, null=True)
    verificado = models.CharField(max_length=1, default='N')
    informativomotorista = models.CharField(max_length=1, default='N')
    informativogrupo = models.CharField(max_length=1, default='N')
    alertasinal = models.IntegerField(default=0)
    acionamentoPamcary = models.IntegerField(default=0)
    email = models.CharField(max_length=1, default='N')
    acionamentoPR = models.IntegerField(default=0)
    data_hora_integrada = models.DateTimeField(default=now, editable=False)
    data_hora_atualizacao = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.descricao
    