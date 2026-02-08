"""URL configuration for test_django project."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# Базовые маршруты проекта: админка и приложение магазина.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shopapp.urls")),
    path("shop/", include("shopapp.urls")),
]

# В режиме разработки подключаем раздачу медиафайлов (изображения товаров).
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
