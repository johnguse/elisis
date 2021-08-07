from django.db import models
from django.utils.timezone import now

class Alertasinal(models.Model):
    idAlertaSinal = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idAlertaSinal')
    placa = models.CharField(max_length=255)
    referencia = models.TextField()
    sessao = models.TextField()
    data_hora_acionamento = models.DateTimeField(default=now, editable=False)
    cancelado = models.IntegerField()
    id_evento = models.IntegerField()

    def __str__(self):
        listagem = "Placa: %s" %self.placa + " | Referência: %s" %self.referencia
        return listagem
        
