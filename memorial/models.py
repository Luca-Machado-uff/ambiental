from django.db import models
# models são a abstração de banco de dados que o Django faz

class Memorias(models.Model):

    nome = models.CharField(max_length=100, null=False, blank=False)
    data_de_nascimento = models.DateField(null=True, blank=True)
    ano_de_nascimento = models.IntegerField(null=True, blank=True, help_text = "Preencher caso o dia exato de nascimento seja desconhecido")
    data_de_falecimento = models.DateField(null=True, blank=True)
    ano_de_falecimento = models.IntegerField(null=True, blank=True, help_text = "Preencher caso o dia exato de falecimento seja desconhecido")
    local_de_nascimento = models.CharField(max_length=100, null=True, blank=True)
    local_de_falecimento = models.CharField(max_length=100, null=True, blank=True)
    descrição = models.TextField(null=True, blank=True)


    #tolook Facilita a visualização ao ser printado na parte do admin
    def __str__(self):
        return self.nome