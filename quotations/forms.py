from django import forms
from .models import Quotation

BASE_INPUT_CLASSES = (
    "w-full rounded-xl border border-slate-300 px-4 py-3 "
    "outline-none transition focus:border-emerald-500 focus:ring-2 focus:ring-emerald-200"
)


class QuotationForm(forms.ModelForm):
    move_type = forms.ChoiceField(
        choices=[("", "Select move type")] + list(Quotation.MoveType.choices),
        widget=forms.Select(attrs={"class": BASE_INPUT_CLASSES})
    )

    property_size = forms.ChoiceField(
        choices=[("", "Select property size")] + list(Quotation.PropertySize.choices),
        widget=forms.Select(attrs={"class": BASE_INPUT_CLASSES})
    )

    class Meta:
        model = Quotation
        fields = [
            "move_type",
            "pickup_location",
            "destination_location",
            "property_size",
            "needs_packing",
            "needs_unpacking",
        ]
        widgets = {
            "pickup_location": forms.TextInput(attrs={
                "class": BASE_INPUT_CLASSES,
                "placeholder": "e.g. Westlands, Nairobi",
            }),
            "destination_location": forms.TextInput(attrs={
                "class": BASE_INPUT_CLASSES,
                "placeholder": "e.g. Syokimau, Machakos",
            }),
            "needs_packing": forms.CheckboxInput(attrs={
                "class": "h-4 w-4 rounded border-slate-300 text-emerald-600 focus:ring-emerald-500"
            }),
            "needs_unpacking": forms.CheckboxInput(attrs={
                "class": "h-4 w-4 rounded border-slate-300 text-emerald-600 focus:ring-emerald-500"
            }),
        }