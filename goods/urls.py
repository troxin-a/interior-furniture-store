from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('search/', views.ProductsListView.as_view(), name='search'),
    path('<slug:category_slug>/', views.ProductsListView.as_view(), name='index'),
    path('product/<slug:product_slug>/', views.ProductsDetailView.as_view(), name='product'),
]
