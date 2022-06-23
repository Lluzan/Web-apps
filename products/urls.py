from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_home, name='product_home'),
    path('<int:pk>', views.UslugaDetailView.as_view(), name='product-detail')
]