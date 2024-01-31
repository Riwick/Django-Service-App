from django.db.models import Prefetch, F

from clients.models import Client
from services.models import Subscription, Plan


def get_subscription_model():
    return Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client', queryset=Client.objects.all().select_related('user').
                 only('company_name', 'user__email'))).annotate(
        price=F('service__full_price') - (F('service__full_price') * F('plan__discount_percent') / 100.00)
    )


