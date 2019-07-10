from django.urls import path

# from .views import ProductDetailView
# from .views import ProductListView
from .views import product_list
from .views import product_detail


urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail')
    # path('', ProductListView.as_view(), name='product-list'),
    # path(
    #     'products/<int:pk>',
    #     ProductDetailView.as_view(),
    #     name='product-detail'),
]
