from django.shortcuts import render

from bookings.forms import BookingForm
from quotations.forms import QuotationForm
from quotations.models import Quotation

# Create your views here.
def home(request):
    quotation_id = request.GET.get("quotation_id")
    quotation_result = None

    if quotation_id:
        quotation_result = Quotation.objects.filter(id=quotation_id).first()

    context = {
        "booking_form": BookingForm(),
        "quotation_form": QuotationForm(),
        "booking_submitted": request.GET.get("booking_submitted") == "1",
        "quotation_submitted": request.GET.get("quotation_submitted") == "1",
        "quotation_result": quotation_result,
    }
    return render(request, "core/home.html", context)