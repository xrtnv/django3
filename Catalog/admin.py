from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = "category"
    search_fields = ("name", "description")

