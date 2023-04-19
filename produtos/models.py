from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=225)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    data_cadastro = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now=True)

    def __repr__(self) -> str:
        return f"<Produto ({self.id}) - {self.nome}>"
