from django.urls import path
from .views import products, categories, pairs

urlpatterns = [
    path('products/', products, name='products'),
    path('categories/', categories, name='categories'),
    path('pairs/', pairs, name='pairs'),
]