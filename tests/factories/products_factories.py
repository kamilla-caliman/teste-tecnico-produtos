from products.models import Product
from categories.models import Category
from django.db.models import QuerySet


def create_multiple_products(product_count: int) -> QuerySet[Product]:
    products_data = [
        {
            "name": f"Produto {index}",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
            "price": 10.80,
        }
        for index in range(1, product_count + 1)
    ]

    product_objects = [Product(**product_data) for product_data in products_data]
    products = Product.objects.bulk_create(product_objects)

    return products


def create_product() -> Product:
    product_data = {
        "name": "Produto test",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "price": 10.80,
    }
    category_data = {"name": "Category test"}

    category = Category.objects.create(**category_data)
    product = Product.objects.create(**product_data)
    product.categories.add(category)

    return product
