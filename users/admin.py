from django.contrib import admin

from habits.models import Habit, Reward
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('email',)


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'action', 'is_nice', 'related_nice_habit', 'reward', 'place', 'time', 'periodicity', 'time_to_implement', 'is_public',)
    list_filter = ('is_nice',)
    search_fields = ('name',)


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')
    list_filter = ('owner',)
    search_fields = ('name',)
