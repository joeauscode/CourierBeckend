from django.urls import path
from .views import *

urlpatterns = [
    # path("tracking/<str:tracking_id>/", TrackingAPIView.as_view(), name="tracking-api"),
    path('tracking/<str:tracking_id>/', TrackingAPIView.as_view(), name='tracking'),
    path("label/", LabelAPIView.as_view(), name="label-api"),
    path("contact/", ContactAPIView.as_view(), name="contact-api"),
    path("phonealart/", PhonealertAPIView.as_view(), name="phonealart"),
    path("ping/", PingAPIView.as_view(), name="ping"),
]


