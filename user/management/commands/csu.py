from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(email="admin@admin.ru")
        user.set_password("120884123qweE")
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
