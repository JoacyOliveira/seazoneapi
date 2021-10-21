from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.core.exceptions import ValidationError

def only_int(value):
    if value.isdigit()==False:
        raise ValidationError('ID contains characters')

# Create your models here.


status = (
    ("Check-In", "Check-In"),
    ("Check-Out", "Check-Out"),
)

class Check(models.Model):

    tipo = models.CharField(max_length=9,choices=status,default="Check-In")
    codigo_quarto = models.CharField(max_length=6)
    quantidade_de_pessoas = models.IntegerField()
    quantida_de_pets = models.IntegerField()
    quantidade_de_diarias = models.IntegerField()
    valor = models.FloatField()
    horario = models.TimeField(default=datetime.now)
    data_checkin = models.DateField()
    data_checkout = models.DateField()
    cidade = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    cep = models.CharField(max_length=8,validators=[only_int])
    codigo_reserva = models.CharField(max_length=10)
    nome_cliente = models.CharField(max_length=50)
    telefone_cliente = PhoneNumberField(null=False, blank=False)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return str(self.codigo_reserva)


class Limpeza(models.Model):

    codigo_quarto = models.CharField(max_length=6)
    horario = models.TimeField(default=datetime.now)
    data_limpeza = models.DateField()
    cidade = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    cep = models.CharField(max_length=8, validators=[only_int])
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return str(self.codigo_quarto)
