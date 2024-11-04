from django.db import models
import secrets

class Convidados(models.Model):
    status_choices = (
        ('AC', 'Aguardando confirmação'),
        ('C', 'Confirmado'),
        ('R', 'Recusado'),
    )

    nome_convidado = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=25, null=True, blank=True)
    maximo_acompanhantes = models.PositiveIntegerField(default=0)
    token = models.CharField(max_length=25, blank=True)  # 'blank=True' permite que o campo fique vazio no formulário
    status = models.CharField(max_length=2, choices=status_choices, default='AC')

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = secrets.token_urlsafe(16)
        super(Convidados, self).save(*args, **kwargs)

    @property
    def link_convite(self):
        return f'http://127.0.0.1:8000/convidados/?token={self.token}'


class Presentes(models.Model):
    nome_presente = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='presentes')
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    importancia = models.PositiveIntegerField()
    reservado = models.BooleanField(default=False)
    reservado_por = models.ForeignKey(Convidados, null=True, blank=True, on_delete=models.DO_NOTHING)  

    def __str__(self):
        return self.nome_presente
