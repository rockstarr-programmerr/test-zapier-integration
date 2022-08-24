import requests
from integration.models import ResthookSubscription, Ticket
from integration.serializers import (ResthookSubscriptionSerializer,
                                     TicketSerializer)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


def send_resthook(event, user, data):
    subscriptions = ResthookSubscription.objects.filter(user=user, event=event)
    for subscription in subscriptions:
        try:
            response = requests.post(subscription.url, data=data)
            print(f'Response from {subscription.url}:', response.status_code, response.content)
        except Exception as e:
            print(e)
            continue


class ResthookScriptionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ResthookSubscriptionSerializer

    def get_queryset(self):
        return ResthookSubscription.objects.filter(user=self.request.user)


class TicketViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        result = super().perform_create(serializer)
        send_resthook('ticket_created', self.request.user, serializer.data)  # Make it a celery task?
        return result
