from django.db import models
from django.contrib.auth.models import User

class SearchedCity(models.Model):
    city_name = models.CharField(unique=True, max_length=100, blank=False)
    search_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Searched City"
        verbose_name_plural = "Searched Cities"

    def __str__(self):
        return self.city_name.capitalize()


class AIWorkoutRecommendation(models.Model):
    weather_condition = models.CharField(max_length=100, blank=False)
    temperature = models.IntegerField(default=0)
    recommendation = models.TextField(blank=False)

    class Meta:
        unique_together = ('weather_condition', 'temperature')
        index_together = ('weather_condition', 'temperature')
        verbose_name = "AI Workout Recommendation"
        verbose_name_plural = "AI Workout Recommendations"


class SavedWorkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.JSONField(blank=False)
    workout_reflection_before = models.TextField(max_length=250, blank=True)
    workout_reflection_after = models.TextField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Saved Workout"
        verbose_name_plural = "Saved Workouts"

    def __str__(self):
        return f"Saved workout {self.id}"


