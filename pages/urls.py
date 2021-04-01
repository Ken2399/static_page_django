# pages/urls.py

from django.urls import path
from .views import ProductPageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('product/', ProductPageView.as_view(), name='product'),
]