from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=225)

    products = models.ManyToManyField("products.Product", related_name="categories")

    def __repr__(self) -> str:
        return f"<Categoria ({self.id}) - {self.name}>"
