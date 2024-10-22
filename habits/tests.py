import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="testuser@mail.ru")
        self.habit = Habit.objects.create(
            name="TestHabit", action="TestAction", owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habit_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], self.habit.name)

    def test_habit_create(self):
        url = reverse("habits:habit_create")
        data = {"name": "Test1Habit", "action": "Test1Action"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        url = reverse("habits:habit_update", args=(self.habit.pk,))
        data = {"name": "AnotherHabit"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "AnotherHabit")

    def test_habit_destroy(self):
        url = reverse("habits:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse("habits:habit_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "name": self.habit.name,
                    "action": self.habit.action,
                    "place": None,
                    "time": self.habit.time,
                    "is_nice": self.habit.is_nice,
                    "periodicity": self.habit.periodicity,
                    "time_to_implement": self.habit.time_to_implement,
                    "is_public": self.habit.is_public,
                    "send_date": datetime.datetime.now().strftime("%Y-%m-%d"),
                    "owner": self.user.pk,
                    "related_nice_habit": self.habit.related_nice_habit,
                    "reward": self.habit.reward,
                },
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class AuthTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="testuser@mail.ru")
        self.habit = Habit.objects.create(name="TestHabit", action="TestAction")

    def test_auth_habit_list(self):
        url = reverse("habits:habit_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
