from django.db import models

# Create your models here.
class Quotation(models.Model):
    class MoveType(models.TextChoices):
        HOME = "home", "Home Relocation"
        OFFICE = "office", "Office Relocation"

    class PropertySize(models.TextChoices):
        BEDSITTER = "bedsitter", "Bedsitter"
        ONE_BEDROOM = "1_bedroom", "1 Bedroom"
        TWO_BEDROOM = "2_bedroom", "2 Bedroom"
        THREE_BEDROOM = "3_bedroom", "3 Bedroom"
        OFFICE_SMALL = "office_small", "Small Office"
        OFFICE_MEDIUM = "office_medium", "Medium Office"

    move_type = models.CharField(max_length=20, choices=MoveType.choices)
    pickup_location = models.CharField(max_length=255)
    destination_location = models.CharField(max_length=255)
    property_size = models.CharField(max_length=30, choices=PropertySize.choices)
    needs_packing = models.BooleanField(default=False)
    needs_unpacking = models.BooleanField(default=False)
    estimated_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_move_type_display()} - KES {self.estimated_amount}"