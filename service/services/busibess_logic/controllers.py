from services.models import Subscription


def get_subscription_model():
    return Subscription.objects.all()