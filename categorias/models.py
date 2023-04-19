from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=225)

    produtos = models.ManyToManyField("produtos.Produto", related_name="categorias")
