from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import BookingForm
from quotations.forms import QuotationForm

# Create your views here.
def submit_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('home')}?booking_submitted=1#booking")

        return render(
            request,
            "core/home.html",
            {
                "booking_form": form,
                "quotation_form": QuotationForm(),
            },
        )

    return redirect(f"{reverse('home')}#booking")