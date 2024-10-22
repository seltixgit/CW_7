from rest_framework.serializers import ModelSerializer

from habits.models import Habit, Reward
from habits.validators import (
    DurationValidator,
    PeriodicityValidator,
    NiceHabitRewardValidator, NiceHabitValidator, RelatedNiceHabitValidator,
)


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            DurationValidator(field="time_to_implement"),
            PeriodicityValidator(field="periodicity"),
            NiceHabitRewardValidator(field1="related_nice_habit", field2="reward"),
            NiceHabitValidator(field1="is_nice", field2="related_nice_habit", field3="reward"),
            RelatedNiceHabitValidator()
        ]


class RewardSerializer(ModelSerializer):
    habits = HabitSerializer(many=True, read_only=True)

    class Meta:
        model = Reward
        fields = "__all__"
