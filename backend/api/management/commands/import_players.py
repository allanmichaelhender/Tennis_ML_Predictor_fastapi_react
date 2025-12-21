import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from api.models import Players

class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = settings.BASE_DIR / 'api' / 'ML_models' / 'data' / 'players_data.csv'
        
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            player_instances = [
                Players(
                    playerID=row['player_id'], 
                    full_name=row['full_name']
                )
                for row in reader
            ]
            Players.objects.bulk_create(player_instances, ignore_conflicts=True)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully imported data from {file_path}'))

