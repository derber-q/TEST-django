from django.contrib import admin

from shopapp.models import Product, ProductAdditionalPhoto


class ProductAdditionalPhotoInline(admin.TabularInline):
    model = ProductAdditionalPhoto
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity_remaining", "quantity_unit", "active_discount", "is_archived")
    list_filter = ("quantity_unit", "is_archived")
    search_fields = ("name", "description")
    inlines = [ProductAdditionalPhotoInline]


@admin.register(ProductAdditionalPhoto)
class ProductAdditionalPhotoAdmin(admin.ModelAdmin):
    list_display = ("product", "id")
    search_fields = ("product__name",)
