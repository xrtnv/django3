from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(email="admin@example.com")
        user.set_password("123")
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
