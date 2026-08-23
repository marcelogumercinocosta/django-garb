from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from datetime import datetime, timezone

from garb.tests.models import Blog, BlogComment, Category


class Command(BaseCommand):
    help = "Create deterministic Django Garb visual-test data."

    def handle(self, *args, **options):
        user_model = get_user_model()
        user, _created = user_model.objects.get_or_create(
            username="garb-admin",
            defaults={"email": "garb@example.com", "is_staff": True, "is_superuser": True},
        )
        user.set_password("garb-admin")
        user.save(update_fields=["password"])

        categories = [
            Category.objects.get_or_create(name=name)[0]
            for name in ("Technology", "Curiosities", "General")
        ]
        for index in range(1, 46):
            blog, _ = Blog.objects.update_or_create(
                name=f"Post {index:02d}",
                defaults={
                    "subtitle": "Lorem ipsum dolor sit amet",
                    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                    "category": categories[index % len(categories)],
                    "published_at": datetime(2026, 8, 20, 12, tzinfo=timezone.utc),
                    "deleted": index % 9 == 0,
                },
            )
            BlogComment.objects.get_or_create(blog=blog, name="Visual comment")

        self.stdout.write(self.style.SUCCESS("Visual fixtures are ready."))
