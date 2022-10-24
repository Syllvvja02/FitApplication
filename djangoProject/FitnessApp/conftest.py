import pytest
from django.contrib.auth.models import User

from FitnessApp.models import Diet, Workout, WarmUp, MyPlan, Stretching, WorkoutExercises, Exercise, WarmupExercises, \
    StretchingInPlan, WorkoutInPlan, Quotes
import random

@pytest.fixture
def quotes():
    random.seed(1)
    lst = []
    for x in range(10):
        q= Quotes.objects.create(quote=f'q{x}')
        lst.append(q)
    return lst


@pytest.fixture
def diet():
    return Diet.objects.create(name='jajko', calories=1000)


@pytest.fixture
def user():
    return User.objects.create_user(username='name', password='pass')

@pytest.fixture
def superuser():
    user = User.objects.create_user(username='name', password='pass')
    user.is_superuser = True
    return user


@pytest.fixture
def plan(user):
    diet = Diet.objects.create(name='jajko', calories=1000)
    myplan = MyPlan.objects.create(name='name', diet=diet, owner=user)
    warmup = WarmUp.objects.create(title='warmup', description='hard warmup')
    workout = Workout.objects.create(title='workout', description='hard workout', warmup=warmup, intensity=1)
    stretch = Stretching.objects.create(title='stretch', description='hard warmup')
    return myplan


@pytest.fixture
def workout():
    warmup = WarmUp.objects.create(title='warmup', description='hard warmup')
    workout = Workout.objects.create(title='workout', description='hard workout', warmup=warmup, intensity=1)
    for x in range(5):
        ex = Exercise.objects.create(name=x, amount=x, time=x, burned_calories=x)
        w_e = WorkoutExercises.objects.create(workout=workout, exercise=ex)
    return workout


@pytest.fixture
def warmup():
    warmup = WarmUp.objects.create(title='warmup', description='hard warmup')
    for x in range(5):
        ex = Exercise.objects.create(name=x, amount=x, time=x, burned_calories=x)
        w_e = WarmupExercises.objects.create(warmup=warmup, exercise=ex)
    return warmup


@pytest.fixture
def stretching():
    return Stretching.objects.create(title='stretch', description='hard warmup')


@pytest.fixture
def plans(user):
    lst = []
    diet = Diet.objects.create(name='jajko', calories=1000)
    for x in range(6):
        lst.append(MyPlan.objects.create(name=x, diet=diet, owner=user))
    return lst


@pytest.fixture
def workouts():
    lst = []
    warmup = WarmUp.objects.create(title='warmup', description='hard warmup')
    for x in range(6):
        lst.append(Workout.objects.create(title=x, description='hard workout', warmup=warmup, intensity=1))
    return lst


@pytest.fixture
def warmups():
    lst = []
    for x in range(6):
        lst.append(WarmUp.objects.create(title='warmup', description='hard warmup'))
    return lst


@pytest.fixture
def strechings():
    lst = []
    for x in range(6):
        lst.append(Stretching.objects.create(title=x, description='softy'))
    return lst

@pytest.fixture
def exercise():
    return Exercise.objects.create(name='x', amount=2, time=2, burned_calories=2)
