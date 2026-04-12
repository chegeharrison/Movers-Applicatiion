from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "phone_number",
        "move_date",
        "move_type",
        "status",
        "created_at",
    )
    list_filter = ("move_type", "status", "move_date", "created_at")
    search_fields = ("full_name", "phone_number", "email", "pickup_location", "destination_location")