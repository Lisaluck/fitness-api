from django.core.management.base import BaseCommand
from bookings.models import FitnessClass
from django.utils import timezone
import pytz


class Command(BaseCommand):
    help = 'Seed initial data for fitness classes'

    def handle(self, *args, **options):
        ist = pytz.timezone('Asia/Kolkata')
        now = timezone.now().astimezone(ist)

        classes = [
            {
                'name': 'Morning Yoga',
                'datetime': now.replace(hour=8, minute=0, second=0, microsecond=0) + timezone.timedelta(days=1),
                'instructor': 'Priya Sharma',
                'capacity': 15,
                'available_slots': 15
            },
            {
                'name': 'Evening Zumba',
                'datetime': now.replace(hour=18, minute=0, second=0, microsecond=0) + timezone.timedelta(days=1),
                'instructor': 'Rahul Verma',
                'capacity': 20,
                'available_slots': 20
            },
            {
                'name': 'HIIT Blast',
                'datetime': now.replace(hour=7, minute=30, second=0, microsecond=0) + timezone.timedelta(days=2),
                'instructor': 'Anjali Patel',
                'capacity': 10,
                'available_slots': 10
            }
        ]

        for cls_data in classes:
            FitnessClass.objects.create(**cls_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded fitness classes data'))