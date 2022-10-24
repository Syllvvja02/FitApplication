import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from FitnessApp.forms import CreateUserForm, CreatePlanForm, LoginForm, AddWorkoutToPlanForm, CreateWarmUpForm, \
    CreateWorkoutForm, CreateStretchForm, AddExercisesToWarmupForm, AddExercisesToWorkoutForm, AddExercisesToStretchForm
from FitnessApp.models import MyPlan, Diet, WorkoutInPlan, WarmUp, Workout, Stretching, WarmupExercises, \
    WorkoutExercises, StretchingExercises


@pytest.mark.django_db
def test_index(quotes):
    client = Client()
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    quote = response.context['q1']
    assert quote.quote == 'q0'


def test_about_us():
    client = Client()
    url = reverse('about_us')
    response = client.get(url)
    assert response.status_code == 200
    # zaliczony


def test_create_user_get():
    client = Client()
    url = reverse('create_user')
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, CreateUserForm)
    # zaliczony


@pytest.mark.django_db
def test_create_user_post():
    client = Client()
    url = reverse('create_user')
    data = {
        'username': 'leo',
        'first_name': 'sylwia',
        'last_name': 'miko',
        'password_one': 'password123',
        'password_two': 'password123',
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert User.objects.get(username='leo', first_name='sylwia', last_name='miko')
    # zaliczony


def test_login_get():
    client = Client()
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, LoginForm)
    # zaliczony


@pytest.mark.django_db
def test_login_post(user):
    client = Client()
    url = reverse('login')
    data = {
        'username': user.username,
        'password': 'pass'  # zapisuje to samo co jest w fiksturze, bo haslo zostaje zahashowane
    }
    response = client.post(url, data)
    assert response.status_code == 302  # przeciez przekierowuje o co chodzi, ale zaliczony


@pytest.mark.django_db
def test_logout(user):
    client = Client()
    url = reverse('logout')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 302  # przeciez przekierowuje o co chodzi, ale zaliczony


@pytest.mark.django_db
def test_homepage(user):
    client = Client()
    url = reverse('homepage')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    # assert 'This is homepage' in str(response.content)
    # zaliczony


@pytest.mark.django_db
def test_create_your_plan_get(user):
    client = Client()
    client.force_login(user)
    url = reverse('create_your_plan')
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, CreatePlanForm)
    # zaliczony


@pytest.mark.django_db
def test_create_your_plan_post(diet, user):
    client = Client()
    client.force_login(user)
    url = reverse('create_your_plan')
    data = {
        'name': 'name',
        'diet': diet.id
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert isinstance(diet, Diet)
    assert MyPlan.objects.create(diet=diet, name='name', owner=user)
    # zaliczony


@pytest.mark.django_db
def test_add_workout_to_plan_get(user):
    client = Client()
    client.force_login(user)
    url = reverse('add_workout_to_plan')
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, AddWorkoutToPlanForm)
    # zaliczony


@pytest.mark.django_db
def test_add_workout_to_plan_post(user, workout, plan):
    client = Client()
    client.force_login(user)
    url = reverse('add_workout_to_plan')
    data = {
        'day': 1,
        'plan': plan.id,
        'workout': workout.id,
        'hour': '8:00'
    }
    response = client.post(url, data)
    assert response.status_code == 200  # zaliczony
    assert WorkoutInPlan.objects.get(day=1, plan=plan, workout=workout, hour='8:00')


@pytest.mark.django_db
def test_show_user_plans(user, plans):
    client = Client()
    client.force_login(user)
    url = reverse('show_user_plan')
    response = client.get(url)
    assert response.status_code == 200
    plans_lst = response.context['user_plan']
    assert plans_lst.count() == len(plans)
    # zaliczony


@pytest.mark.django_db
def test_all_workouts(user, workouts):
    client = Client()
    client.force_login(user)
    url = reverse('show_all_workouts')
    response = client.get(url)
    assert response.status_code == 200
    workouts_lst = response.context['all_workouts']
    assert workouts_lst.count() == len(workouts)
    # zaliczony


@pytest.mark.django_db
def test_all_warmups(user, warmups):
    client = Client()
    client.force_login(user)
    url = reverse('show_all_warmups')
    response = client.get(url)
    assert response.status_code == 200
    warmups_lst = response.context['all_warmups']
    assert warmups_lst.count() == len(warmups)
    # zaliczony


@pytest.mark.django_db
def test_all_stretchings(user, strechings):
    client = Client()
    client.force_login(user)
    url = reverse('show_all_stretch')
    response = client.get(url)
    assert response.status_code == 200
    stretch_lst = response.context['all_stretch']
    assert stretch_lst.count() == len(strechings)
    # zaliczony


@pytest.mark.django_db
def test_show_details_ex_workout(user, workout):
    client = Client()
    client.force_login(user)
    url = reverse('workout_details', args=(workout.id,))
    response = client.get(url)
    assert response.status_code == 200
    workout_details = response.context['exercises']
    assert workout_details.count() == len(workout.exercises.all())
    # zaliczony


@pytest.mark.django_db
def test_show_details_ex_warmup(user, warmup):
    client = Client()
    client.force_login(user)
    url = reverse('warmup_details', args=(warmup.id,))
    response = client.get(url)
    assert response.status_code == 200
    warmup_details = response.context['exercises']
    assert warmup_details.count() == len(warmup.exercises.all())
    # zaliczony


@pytest.mark.django_db
def test_show_details_ex_stretching(user, stretching):
    client = Client()
    client.force_login(user)
    url = reverse('stretch_details', args=(stretching.id,))
    response = client.get(url)
    assert response.status_code == 200
    stretch_details = response.context['exercises']
    assert stretch_details.count() == len(stretching.exercises.all())
    # zaliczony


@pytest.mark.django_db
def test_plan_details(user, plan):
    client = Client()
    client.force_login(user)
    url = reverse('plan_details', args=(plan.id,))
    response = client.get(url)
    assert response.status_code == 200
    workouts = response.context['workouts']
    stretchings = response.context['stretchings']
    assert workouts.count() == len(plan.workout.all())
    assert stretchings.count() == len(plan.stretching.all())
    # zaliczony


@pytest.mark.django_db
def test_delete_plan(user, plan):
    client = Client()
    client.force_login(user)
    url = reverse('delete_plan', args=(plan.id,))
    response = client.get(url)
    assert response.status_code == 302
    # zaliczony, tylko pytanie jak napisac sprawdzenie czy plan sie usuwa czy nie


@pytest.mark.django_db
def test_delete_warmup(admin_user, warmup):
    client = Client()
    client.force_login(admin_user)
    url = reverse('delete_warmup', args=(warmup.id,))
    response = client.get(url)
    assert response.status_code == 302
    # zaliczony


@pytest.mark.django_db
def test_delete_workout(admin_user, workout):
    client = Client()
    client.force_login(admin_user)
    url = reverse('delete_workout', args=(workout.id,))
    response = client.get(url)
    assert response.status_code == 302
    # zaliczony


@pytest.mark.django_db
def test_delete_warmup(admin_user, stretching):
    client = Client()
    client.force_login(admin_user)
    url = reverse('delete_stretch', args=(stretching.id,))
    response = client.get(url)
    assert response.status_code == 302
    # zaliczony


@pytest.mark.django_db
def test_create_warmup_get(admin_user):
    client = Client()
    client.force_login(admin_user)
    url = reverse('create_warmup')
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, CreateWarmUpForm)
    # zaliczony


@pytest.mark.django_db
def test_create_warmup_post(admin_user):
    client = Client()
    client.force_login(admin_user)
    url = reverse('create_warmup')
    data = {
        'title': 'title',
        'description': 'description'
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert WarmUp.objects.get(title='title', description='description')
    # zaliczony


@pytest.mark.django_db
def test_create_workout_get(admin_user):
    client = Client()
    client.force_login(admin_user)
    url = reverse('create_workout')
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, CreateWorkoutForm)
    # zaliczony


@pytest.mark.django_db
def test_create_warmup_post(admin_user, warmup):
    client = Client()
    client.force_login(admin_user)
    url = reverse('create_workout')
    data = {
        'title': 'title',
        'description': 'description',
        'warmup': warmup.id,
        'intensity': 1
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert Workout.objects.get(title='title', description='description', warmup=warmup, intensity=1)
    # zaliczony


@pytest.mark.django_db
def test_create_warmup_get(admin_user):
    client = Client()
    client.force_login(admin_user)
    url = reverse('create_stretch')
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, CreateStretchForm)
    # zaliczony


@pytest.mark.django_db
def test_create_warmup_post(admin_user):
    client = Client()
    client.force_login(admin_user)
    url = reverse('create_stretch')
    data = {
        'title': 'title',
        'description': 'description'
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert Stretching.objects.get(title='title', description='description')
    # zaliczony


@pytest.mark.django_db
def test_add_exercises_to_warmup_get(admin_user, warmup):
    client = Client()
    client.force_login(admin_user)
    url = reverse('add_exercises_to_warmup', args=(warmup.id,))
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, AddExercisesToWarmupForm)
    # zaliczony


@pytest.mark.django_db
def test_add_exercises_to_warmup_post(admin_user, warmup, exercise):
    client = Client()
    client.force_login(admin_user)
    url = reverse('add_exercises_to_warmup', args=(warmup.id,))
    data = {
        'exercise': exercise.id
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert WarmupExercises.objects.get(exercise=exercise, warmup=warmup)
    # zaliczony


@pytest.mark.django_db
def test_add_exercises_to_workout_get(admin_user, workout):
    client = Client()
    client.force_login(admin_user)
    url = reverse('add_exercises_to_workout', args=(workout.id,))
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, AddExercisesToWorkoutForm)
    # zaliczony


@pytest.mark.django_db
def test_add_exercises_to_workout_post(admin_user, workout, exercise):
    client = Client()
    client.force_login(admin_user)
    url = reverse('add_exercises_to_workout', args=(workout.id,))
    data = {
        'exercise': exercise.id
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert WorkoutExercises.objects.get(exercise=exercise, workout=workout)
    # zaliczony


@pytest.mark.django_db
def test_add_exercises_to_stretch_get(admin_user, stretching):
    client = Client()
    client.force_login(admin_user)
    url = reverse('add_exercises_to_stretching', args=(stretching.id,))
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, AddExercisesToStretchForm)
    # zaliczony


@pytest.mark.django_db
def test_add_exercises_to_stretch_post(admin_user, stretching, exercise):
    client = Client()
    client.force_login(admin_user)
    url = reverse('add_exercises_to_stretching', args=(stretching.id,))
    data = {
        'exercise': exercise.id
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert StretchingExercises.objects.get(exercise=exercise, stretching=stretching)
    # zaliczony
