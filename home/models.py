from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.categoria

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.FloatField()
    imagem = models.ImageField(upload_to="img_produtos")

    def __str__(self):
        return self.nome