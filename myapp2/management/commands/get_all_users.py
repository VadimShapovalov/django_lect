from django.core.management.base import BaseCommand

# from lectionsgb.myapp2.models import User

from myapp2.models import User


class Command(BaseCommand):
    help = "Get all users"

    def handle(self, *args, **kwargs):
        users = User.objects.all()

        self.stdout.write(f'{users}')