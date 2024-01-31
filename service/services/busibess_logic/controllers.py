from django.db.models import Prefetch

from clients.models import Client
from services.models import Subscription


def get_subscription_model():
    return Subscription.objects.all().prefetch_related(
        Prefetch('client', queryset=Client.objects.all().select_related('user').
                 only('company_name', 'user__email')))
