# product_app/urls.py

from django.urls import path, include
from rest_framework import routers
from .views import ProductsView

router = routers.SimpleRouter()
router.register(r'products', ProductsView, basename='products')

urlpatterns = [
    path('', include(router.urls)),  # Incluir las URLs del router
]
