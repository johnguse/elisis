from django.db import models
from django.utils.timezone import now

class Naoconformidade(models.Model):
    CodigoViagem = models.IntegerField()
    DataCadastro = models.DateTimeField(blank=True, null=True)
    Descricao = models.CharField(max_length=255)
    DescricaoTipoNC = models.CharField(max_length=255)
    Placa = models.CharField(max_length=20)
    TipoNC = models.IntegerField()
    data_alteracao = models.DateTimeField(blank=True, null=True)
    idNC = models.IntegerField()
    ornc_data_leitura_gr = models.CharField(max_length=255)
    ornc_data_leitura_site = models.CharField(max_length=255)
    ornc_esis_codigo = models.CharField(max_length=255)
    ornc_usua_pfis_pess_oras_codigo = models.IntegerField()
    usua_login = models.CharField(max_length=255)
    usua_pess_nome = models.CharField(max_length=255)
    informativogrupo = models.CharField(max_length=1, default='N')
    data_hora_integrada = models.DateTimeField(default=now, editable=False)
    data_hora_atualizacao = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        nc = "Placa: %s" %self.Placa + " | NC: %s" %self.DescricaoTipoNC
        return nc
        
