from products.models import Product
from categories.models import Category
from django.db.models import QuerySet


def create_multiple_products(product_count: int) -> QuerySet[Product]:
    # category_data = {"name": "Categoria teste"}
    # category = Category.objects.create(**category_data)
    products_data = [
        {
            "name": f"Produto {index}",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
            "price": 10.80,
        }
        for index in range(1, product_count + 1)
    ]

    # for product_data in products_data:
    #     product_objects = Product.objects.create(**product_data)
    #     product_objects.categories.add(category)

    product_objects = [Product(**product_data) for product_data in products_data]
    products = Product.objects.bulk_create(product_objects)

    return products
