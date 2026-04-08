from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as octo_models

from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User = get_user_model()
        User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Create teams
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='password', team=marvel)
        steve = User.objects.create_user(username='cap', email='steve@marvel.com', password='password', team=marvel)
        bruce = User.objects.create_user(username='batman', email='bruce@dc.com', password='password', team=dc)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='password', team=dc)

        # Create activities
        octo_models.Activity.objects.create(user=tony, type='run', duration=30, distance=5)
        octo_models.Activity.objects.create(user=steve, type='cycle', duration=60, distance=20)
        octo_models.Activity.objects.create(user=bruce, type='swim', duration=45, distance=2)
        octo_models.Activity.objects.create(user=clark, type='run', duration=50, distance=10)

        # Create workouts
        octo_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        octo_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Create leaderboard
        octo_models.Leaderboard.objects.create(user=tony, points=100)
        octo_models.Leaderboard.objects.create(user=steve, points=90)
        octo_models.Leaderboard.objects.create(user=bruce, points=95)
        octo_models.Leaderboard.objects.create(user=clark, points=110)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
