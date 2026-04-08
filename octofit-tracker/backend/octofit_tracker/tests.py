from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='TestTeam')
        self.assertEqual(str(t), 'TestTeam')
    def test_user_create(self):
        t = Team.objects.create(name='T')
        u = User.objects.create(username='u', team=t)
        self.assertEqual(u.team, t)
    def test_activity_create(self):
        t = Team.objects.create(name='T')
        u = User.objects.create(username='u', team=t)
        a = Activity.objects.create(user=u, type='run', duration=10, distance=1.5)
        self.assertEqual(str(a), 'u - run')
    def test_workout_create(self):
        w = Workout.objects.create(name='W', description='desc', duration=20)
        self.assertEqual(str(w), 'W')
    def test_leaderboard_create(self):
        t = Team.objects.create(name='T')
        u = User.objects.create(username='u', team=t)
        l = Leaderboard.objects.create(user=u, points=42)
        self.assertEqual(str(l), 'u: 42')
