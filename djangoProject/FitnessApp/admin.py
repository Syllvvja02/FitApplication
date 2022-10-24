from django.contrib import admin

from FitnessApp.models import *

admin.site.register(Quotes)
admin.site.register(Exercise)
admin.site.register(WarmUp)
admin.site.register(Workout)
admin.site.register(Stretching)
admin.site.register(Diet)

admin.site.register(MyPlan)
admin.site.register(WorkoutInPlan)
admin.site.register(StretchingInPlan)
admin.site.register(WarmupExercises)
admin.site.register(WorkoutExercises)
admin.site.register(StretchingExercises)



# Register your models here.
