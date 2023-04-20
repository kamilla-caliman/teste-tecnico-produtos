from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __repr__(self) -> str:
        return f"<Produto ({self.id}) - {self.name}>"
