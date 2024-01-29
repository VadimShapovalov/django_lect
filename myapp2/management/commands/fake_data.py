from django.core.management.base import BaseCommand

# from lectionsgb.myapp2.models import User

from myapp2.models import Author, Post


class Command(BaseCommand):
    help = "Generate fake authors and posts"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Name{i}', email=f'Email{i}@example.com')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title{i}',
                    content=f'Text from {author.name} #{j} is bla bla bla',
                    author=author
                )
                post.save()
