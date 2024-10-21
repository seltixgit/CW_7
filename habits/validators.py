from rest_framework import serializers


class DurationValidator:
    """Проверка длительности более 120 секунд"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)
        if val and val > 120:
            raise serializers.ValidationError(
                f"{self.field} не должно превышать 120 секунд"
            )


class PeriodicityValidator:
    """Проверка периодичности не реже 1 раза в 7 дней"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)
        if val and val > 7:
            raise serializers.ValidationError(f"{self.field} не должно быть больше 7")


class NiceHabitRewardValidator:
    """Проверка одновременного выбора приятной привычки и вознаграждения"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

        def __call__(self, value):
            if dict(value).get(self.field1) and dict(value).get(self.field2):
                raise serializers.ValidationError(
                    "Выберите или приятную привычку, или вознаграждение"
                )


class RelatedNiceHabitValidator:
    """Проверка связанной приятной привычки"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        val = dict(value).get(self.field1)
        if val:
            if not dict(value).get(self.field2):
                raise serializers.ValidationError(
                    f"В связанные привычки могут попадать только привычки с признаком приятной привычки"
                )


class NiceHabitValidator:
    """Проверка приятной привычки"""

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        if (
                dict(value).get(self.field1)
                and dict(value).get(self.field2)
                or dict(value).get(self.field1)
                and dict(value).get(self.field3)
        ):
            raise serializers.ValidationError(
                "У приятной привычки не может быть ни вознаграждения, ни связанной привычки"
            )
