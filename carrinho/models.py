from django.db import models
from home.models import Produto

class Carrinho(models.Model):
    produtos_carrinho = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return self.produtos_carrinho.nome
    

    class Meta:
        verbose_name_plural = "Carrinho"