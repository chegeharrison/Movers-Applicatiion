from django.db import models

# Create your models here.
class Booking(models.Model):
    class MoveType(models.TextChoices):
        HOME = "home", "Home Relocation"
        OFFICE = "office", "Office Relocation"

    class BookingStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        IN_PROGRESS = "in_progress", "In Progress"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    move_date = models.DateField()
    move_type = models.CharField(max_length=20, choices=MoveType.choices)
    pickup_location = models.CharField(max_length=255)
    destination_location = models.CharField(max_length=255)
    special_instructions = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=BookingStatus.choices,
        default=BookingStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.move_date} - {self.get_move_type_display()}"
