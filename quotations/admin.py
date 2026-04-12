from django.contrib import admin
from .models import Quotation


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = (
        "move_type",
        "pickup_location",
        "destination_location",
        "property_size",
        "estimated_amount",
        "created_at",
    )
    list_filter = ("move_type", "property_size", "created_at")
    search_fields = ("pickup_location", "destination_location")