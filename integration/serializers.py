from integration.models import ResthookSubscription, Ticket
from rest_framework import serializers


class ResthookSubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ResthookSubscription
        fields = ['id', 'event', 'url', 'user']


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ticket
        fields = ['id', 'name', 'user']
