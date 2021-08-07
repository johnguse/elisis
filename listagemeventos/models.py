from django.db import models
from django.utils.timezone import now

class Listagemeventos(models.Model):
    idListagemEventos = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idListagemEventos')
    tipo_evento = models.IntegerField()
    descricao_tipo_evento = models.CharField(max_length=255)
    base = models.IntegerField(blank=True, null=True)

    def __str__(self):
        listagem = "Tipo: %s" %self.tipo_evento + " | Evento: %s" %self.descricao_tipo_evento
        return listagem
        
