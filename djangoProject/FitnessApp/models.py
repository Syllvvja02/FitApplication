from django.contrib.auth.models import User
from django.db import models


class Quotes(models.Model):
    quote = models.TextField(max_length=250, unique=True)
    author = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.quote}'


class Exercise(models.Model):
    name = models.CharField(max_length=32)
    amount = models.PositiveIntegerField()
    time = models.PositiveIntegerField()
    burned_calories = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} x {self.amount} for {self.time} seconds'


class WarmUp(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=200)
    exercises = models.ManyToManyField(Exercise, through='WarmupExercises')

    def __str__(self):
        return f'{self.title}'


intensity_choice = (
    (1, 'for begginers'),
    (2, 'for begginers and more advanced ones'),
    (3, 'for advanced ones')
)


class Workout(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=200)
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercises')
    intensity = models.IntegerField(choices=intensity_choice)  # get_intensity_display
    warmup = models.ForeignKey(WarmUp, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Stretching(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=200)
    exercises = models.ManyToManyField(Exercise, through='StretchingExercises')

    def __str__(self):
        return f'{self.title}'


class Diet(models.Model):
    name = models.CharField(max_length=32)
    calories = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.calories} kcal.'


class MyPlan(models.Model):
    name = models.CharField(max_length=64, default='My plan')
    workout = models.ManyToManyField(Workout, through='WorkoutInPlan', blank=True)
    stretching = models.ManyToManyField(Stretching, through='StretchingInPlan', blank=True)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


day_choice = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
)


class WorkoutInPlan(models.Model):
    day = models.IntegerField(choices=day_choice)  # get_dey_display
    plan = models.ForeignKey(MyPlan, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    hour = models.CharField(max_length=8, default='8:00', blank=True)


class StretchingInPlan(models.Model):
    day = models.IntegerField(choices=day_choice)
    plan = models.ForeignKey(MyPlan, on_delete=models.CASCADE)
    stretching = models.ForeignKey(Stretching, on_delete=models.CASCADE)
    hour = models.CharField(max_length=8, default='7:00', blank=True)


class WarmupExercises(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    warmup = models.ForeignKey(WarmUp, on_delete=models.CASCADE)


class WorkoutExercises(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)


class StretchingExercises(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    stretching = models.ForeignKey(Stretching, on_delete=models.CASCADE)
