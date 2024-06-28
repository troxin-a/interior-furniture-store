from django.urls import path
from users import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('logout/', views.logout, name='logout'),
]
