"""URL configuration for test_django project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("shop/", include("shopapp.urls")),
]
