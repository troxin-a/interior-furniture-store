"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

import config.settings as settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path("catalog/", include("goods.urls", namespace="catalog")),
    path("user/", include("users.urls", namespace="user")),
    path("cart/", include("carts.urls", namespace="cart")),
    path("orders/", include("orders.urls", namespace="orders")),
    # path(адрес приложения / подключаемый файл / Пространство имен для разграничения)
]

if settings.DEBUG:
    # Приложение для отладки
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    # Соответствие между URL и путями к файлам, указанных в settings
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
