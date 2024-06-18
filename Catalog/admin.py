from django.contrib import admin
from Catalog.models import Product, Category, Version
from user.models import User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "version_name", "version_number")
    list_filter = ("product", "version_name", "version_number")
    search_fields = ("id", "product", "version_name")
