from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ResthookSubscription(models.Model):
    class EventType(models.TextChoices):
        TICKET_CREATED = 'ticket_created'

    event = models.CharField(max_length=50, choices=EventType.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=255)


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
