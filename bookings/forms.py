from django import forms
from .models import Booking

BASE_INPUT_CLASSES = (
    "w-full rounded-xl border border-slate-300 px-4 py-3 "
    "outline-none transition focus:border-emerald-500 focus:ring-2 focus:ring-emerald-200"
)


class BookingForm(forms.ModelForm):
    move_type = forms.ChoiceField(
        choices=[("", "Select move type")] + list(Booking.MoveType.choices),
        widget=forms.Select(attrs={"class": BASE_INPUT_CLASSES})
    )

    move_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": BASE_INPUT_CLASSES})
    )

    class Meta:
        model = Booking
        fields = [
            "full_name",
            "phone_number",
            "email",
            "move_date",
            "move_type",
            "pickup_location",
            "destination_location",
            "special_instructions",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": BASE_INPUT_CLASSES,
                "placeholder": "Enter your full name",
            }),
            "phone_number": forms.TextInput(attrs={
                "class": BASE_INPUT_CLASSES,
                "placeholder": "+254...",
            }),
            "email": forms.EmailInput(attrs={
                "class": BASE_INPUT_CLASSES,
                "placeholder": "name@example.com",
            }),
            "pickup_location": forms.TextInput(attrs={
                "class": BASE_INPUT_CLASSES,
                "placeholder": "Enter pickup location",
            }),
            "destination_location": forms.TextInput(attrs={
                "class": BASE_INPUT_CLASSES,
                "placeholder": "Enter destination location",
            }),
            "special_instructions": forms.Textarea(attrs={
                "class": BASE_INPUT_CLASSES,
                "rows": 4,
                "placeholder": "Add any special instructions",
            }),
        }