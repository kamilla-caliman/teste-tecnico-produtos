from categories.models import Category
from django.db.models import QuerySet


def create_multiple_categories(category_count: int) -> QuerySet[Category]:
    categories_data = [
        {"name": f"Category {index}"} for index in range(1, category_count + 1)
    ]

    category_objects = [Category(**category_data) for category_data in categories_data]
    categories = Category.objects.bulk_create(category_objects)

    return categories


def create_category() -> Category:
    category_data = {"name": "Category test"}

    category = Category.objects.create(**category_data)
    return category
