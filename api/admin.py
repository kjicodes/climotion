from django.contrib import admin
from api.models import SearchedCity, SavedWorkout, AIWorkoutRecommendation

admin.site.register(SearchedCity)
admin.site.register(SavedWorkout)
admin.site.register(AIWorkoutRecommendation)
