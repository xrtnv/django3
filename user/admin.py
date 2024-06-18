from django.contrib import admin

from user.models import User


@admin.register(User)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone_number", "country",)
    list_filter = ("id", "email", "phone_number", "country",)
    search_fields = ("id", "email", "phone_number", "country",)
