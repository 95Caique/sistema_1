from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


class Servidor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[MinLengthValidator(11), MaxLengthValidator(11)]
    )
    matricula = models.CharField(
        max_length=6,
        unique=True,
        validators=[MinLengthValidator(6), MaxLengthValidator(6)]
    )
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nome} - Matrícula: {self.matricula}"