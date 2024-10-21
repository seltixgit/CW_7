from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.serializer import RewardViewSet
from habits.views import (
    HabitListAPIView,
    HabitCreateAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
)

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r"reward", RewardViewSet, basename="reward")

urlpatterns = [
    path("", HabitListAPIView.as_view(), name="habit_list"),
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_retrieve"),
    path("<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit_delete"),
] + router.urls
