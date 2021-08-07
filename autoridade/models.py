from django.db import models
from django.utils.timezone import now

class Autoridade(models.Model):
    idAutoridade = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idAutoridade')
    nomeAutoridade = models.CharField(max_length=255)
    descricao = models.TextField()
    sigla = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    emails = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    data_hora_cadastro = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        autoridade = "Autoridade: %s" %self.nomeAutoridade + " | Telefone: %s" %self.telefone
        return autoridade
        
