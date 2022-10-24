from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from FitnessApp.models import MyPlan, WorkoutInPlan, StretchingInPlan, Workout, WorkoutExercises, WarmUp, \
    WarmupExercises, Stretching, StretchingExercises


def validate_password(value):
    if len(value) < 8:
        raise ValidationError('Password is too short')


def check_if_has_number(value):
    if not any(x for x in value if x.isdigit()):
        raise ValidationError('Password should have a number')


class CreateUserForm(forms.ModelForm):
    password_one = forms.CharField(label='Password', help_text='Password must be longer than 8 characters',
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                   validators=[validate_password, check_if_has_number])
    password_two = forms.CharField(label='re-Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        data = super().clean()
        pass1 = data.get('password_one')
        if pass1 is not None and pass1 != data.get('password_two'):
            raise ValidationError('Passwords are not the same.')
        return data


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-control'}),
                               required=False)


class CreatePlanForm(forms.ModelForm):
    class Meta:
        model = MyPlan
        fields = ['name', 'diet']


class AddWorkoutToPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutInPlan
        fields = '__all__'


class AddStretchingToPlanForm(forms.ModelForm):
    class Meta:
        model = StretchingInPlan
        fields = '__all__'


class CreateWarmUpForm(forms.ModelForm):
    class Meta:
        model = WarmUp
        fields = ['title', 'description']


class AddExercisesToWarmupForm(forms.ModelForm):
    class Meta:
        model = WarmupExercises
        fields = ['exercise']


class CreateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'description', 'intensity', 'warmup']


class AddExercisesToWorkoutForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercises
        fields = ['exercise']


class CreateStretchForm(forms.ModelForm):
    class Meta:
        model = Stretching
        fields = ['title', 'description']


class AddExercisesToStretchForm(forms.ModelForm):
    class Meta:
        model = StretchingExercises
        fields = ['exercise']
