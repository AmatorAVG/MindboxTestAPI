from django.http import HttpResponse
from goods.models import Product
from goods.models import Category


def products(request):
    resp = HttpResponse("Список всех продуктов с их категориями:\n", content_type='text/plain; charset=utf-8')

    for product in Product.objects.all():
        resp.write(f"\n{product.name}\n")
        for category in product.category_set.all():
            resp.write(f"   {category.name}\n")
    return resp


def categories(request):
    resp = HttpResponse("Список всех категорий с продуктами:\n", content_type='text/plain; charset=utf-8')

    for category in Category.objects.all():
        resp.write(f"\n{category.name}\n")
        for product in category.products.all():
            resp.write(f"   {product.name}\n")
    return resp


def pairs(request):
    resp = HttpResponse("Список всех пар «Имя продукта – Имя категории»:\n", content_type='text/plain; charset=utf-8')

    for product in Product.objects.all():
        if product.category_set.exists():
            for category in product.category_set.all():
                resp.write(f"{product.name} - {category.name}\n")
    return resp
