from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                password='complexpassword123'
            )
        print('Superuser has been created.')
