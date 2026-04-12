from django.urls import path
from .views import submit_booking

urlpatterns = [
    path("submit/", submit_booking, name="submit_booking"),
]