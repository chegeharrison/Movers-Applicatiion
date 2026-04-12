from django.urls import path
from .views import submit_quotation

urlpatterns = [
    path("submit/", submit_quotation, name="submit_quotation"),
]