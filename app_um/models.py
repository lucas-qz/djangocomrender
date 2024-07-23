#/////////////////////////////////////////////////////////////////////////////////////////////////
#---- USANDO FUNÇÕES PARA CRIAR AS VIEWS -----------
from django.db import models
class Musica(models.Model): 
    musica = models.CharField(max_length=50)
    cantor = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.musica}"



#/////////////////////////////////////////////////////////////////////////////////////////////////
#---- USANDO CLASSES PARA CRIAR AS VIEWS -----------
class Musica2(models.Model): 
    musica = models.CharField(max_length=50)
    cantor = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.musica}"
#///////////////////////////////////////////////////////////////////////////////////////////////// 