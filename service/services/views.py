from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet


from .busibess_logic.controllers import *
from .serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = get_subscription_model()
    serializer_class = SubscriptionSerializer
