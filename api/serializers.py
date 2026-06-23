import re
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from api.models import SearchedCity, SavedWorkout, AIWorkoutRecommendation


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email", "password", "confirm_password"]
        extra_kwargs = {
            "first_name": { "required": True },
            "last_name": { "required": True },
            "email": {
                "required": True,
                "validators": [UniqueValidator(queryset=User.objects.all())],
            },
            "password": {
                "write_only": True,
                "required": True
            }
        }

    def validate_first_name(self, value):
        if not re.match(r'^(?=.*[A-Za-z])[A-Za-z\s\-]+$', value):
            raise serializers.ValidationError("First name must contain only letters.")
        return value

    def validate_last_name(self, value):
        if not re.match(r'^(?=.*[A-Za-z])[A-Za-z\s\-]+$', value):
            raise serializers.ValidationError("Last name must contain only letters.")
        return value

    def validate_password(self, value):
        if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$', value):
            raise serializers.ValidationError("Password must be at least 8 characters and contain an uppercase letter, lowercase letter, number, and special character (@$!%*?&).")
        return value

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"confirm_password": "Password does not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        new_user = User.objects.create_user(**validated_data)
        return new_user


class SearchedCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchedCity
        fields = ["id", "city_name"]


class AIWorkoutRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIWorkoutRecommendation
        fields = ["id", "weather_condition", "temperature", "recommendation"]


class SavedWorkoutSerializer(serializers.ModelSerializer):
    workout_reflection = serializers.SerializerMethodField()

    class Meta:
        model = SavedWorkout
        fields = ["id", "user", "workout", "workout_reflection_before", "workout_reflection_after", "workout_reflection", "created_at"]
        extra_kwargs = {
            "user": {
                "read_only": True
            },
            "workout_reflection_before": {
                "write_only": True
            },
            "workout_reflection_after": {
                "write_only": True
            }
        }


    def get_workout_reflection(self, obj):
        return {
            "before_workout": obj.workout_reflection_before,
            "after_workout": obj.workout_reflection_after
            }
