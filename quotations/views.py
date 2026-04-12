from django.shortcuts import redirect, render
from django.urls import reverse

from bookings.forms import BookingForm
from .forms import QuotationForm
from .services import calculate_estimate


def submit_quotation(request):
    if request.method == "POST":
        form = QuotationForm(request.POST)
        if form.is_valid():
            quotation = form.save(commit=False)
            quotation.estimated_amount = calculate_estimate(form.cleaned_data)
            quotation.save()
            return redirect(
                f"{reverse('home')}?quotation_submitted=1&quotation_id={quotation.id}#quotation"
            )

        return render(
            request,
            "core/home.html",
            {
                "quotation_form": form,
                "booking_form": BookingForm(),
            },
        )

    return redirect(f"{reverse('home')}#quotation")