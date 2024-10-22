from celery import shared_task

import datetime

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_habit():
    habits = Habit.objects.all()
    current_date = datetime.datetime.now().date()
    current_time = datetime.datetime.now()
    for habit in habits:
        tg_chat_id = habit.owner.tg_chat_id
        if (
            habit.send_date == current_date
            and habit.time.hour == current_time.hour
            and habit.time.minute == current_time.minute
            and habit.reward
        ):
            message = f"Я буду {habit.action} в {habit.time} в {habit.place} и получу за это {habit.reward.name}"
            send_telegram_message(message, tg_chat_id)
            periodicity = habit.periodicity
            habit.send_date += datetime.timedelta(days=periodicity)
            habit.save()
            print(habit.send_date)
        elif (
            habit.send_date == current_date
            and habit.time.hour == current_time.hour
            and habit.time.minute == current_time.minute
            and habit.related_nice_habit
        ):
            message = f"Я буду {habit.action} в {habit.time} в {habit.place} и получу за это {habit.related_nice_habit.name}"
            send_telegram_message(message, tg_chat_id)
            periodicity = habit.periodicity
            habit.send_date += datetime.timedelta(days=periodicity)
            habit.save()
            print(habit.send_date)
