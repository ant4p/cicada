from django.urls import path

from products.views import ProductsListView, ProductView

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('<slug:slug>/', ProductView.as_view(), name='product')
]