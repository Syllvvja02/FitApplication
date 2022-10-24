"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from FitnessApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    path('aboutus/', views.AboutUs.as_view(), name='about_us'),
    path('createuser/', views.CreateUserView.as_view(), name='create_user'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('homepage/', views.HomepageView.as_view(), name='homepage'),
    path('createyourplan/', views.CreateYourPlan.as_view(), name='create_your_plan'),
    path('addworkoutoplan/', views.AddWorkoutToPlan.as_view(), name='add_workout_to_plan'),
    path('addstretchingtoplan/', views.AddStretchingToPlan.as_view(), name='add_stretching_to_plan'),
    path('show_plan/', views.ShowUserPlan.as_view(), name='show_user_plan'),
    path('show_workouts/', views.AllWorkouts.as_view(), name='show_all_workouts'),
    path('show_warmups/', views.AllWarmups.as_view(), name='show_all_warmups'),
    path('show_stretchings/', views.AllStretchings.as_view(), name='show_all_stretch'),
    path('workout_details/<int:train_id>/', views.ShowExercisesDetails_Workout.as_view(), name='workout_details'),
    path('warmup_details/<int:train_id>/', views.ShowExercisesDetails_Warmup.as_view(), name='warmup_details'),
    path('stretch_details/<int:train_id>/', views.ShowExercisesDetails_Stretch.as_view(), name='stretch_details'),
    path('plan_details/<int:planed_id>/', views.MyPlanDetails.as_view(), name='plan_details'),
    path('delete_plan/<int:plan_id>/', views.DeletePlan.as_view(), name='delete_plan'),
    path('delete_workout/<int:workout_id>/', views.DeleteWorkout.as_view(), name='delete_workout'),
    path('delete_warmup/<int:warmup_id>/', views.DeleteWarmup.as_view(), name='delete_warmup'),
    path('delete_stretch/<int:stretch_id>/', views.DeleteStretching.as_view(), name='delete_stretch'),
    path('create_warmup/', views.CreateWarmUp.as_view(), name='create_warmup'),
    path('warmup_add_exercises/<int:warmup_id>/', views.AddExercise_toWarmup.as_view(), name='add_exercises_to_warmup'),
    path('create_workout/', views.CreateWorkout.as_view(), name='create_workout'),
    path('workout_add_exercises/<int:workout_id>/', views.AddExercise_toWorkout.as_view(), name='add_exercises_to_workout'),
    path('create_stretch/', views.CreateStretching.as_view(), name='create_stretch'),
    path('stretch_add_exercises/<int:stretch_id>/', views.AddExercise_toStretching.as_view(), name='add_exercises_to_stretching'),
]
