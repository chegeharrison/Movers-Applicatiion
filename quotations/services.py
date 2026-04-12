from decimal import Decimal


def calculate_estimate(cleaned_data):
    move_type = cleaned_data.get("move_type")
    property_size = cleaned_data.get("property_size")
    needs_packing = cleaned_data.get("needs_packing")
    needs_unpacking = cleaned_data.get("needs_unpacking")

    move_type_prices = {
        "home": Decimal("5000"),
        "office": Decimal("12000"),
    }

    property_size_prices = {
        "bedsitter": Decimal("2000"),
        "1_bedroom": Decimal("4000"),
        "2_bedroom": Decimal("7000"),
        "3_bedroom": Decimal("10000"),
        "office_small": Decimal("6000"),
        "office_medium": Decimal("10000"),
    }

    total = Decimal("0")
    total += move_type_prices.get(move_type, Decimal("0"))
    total += property_size_prices.get(property_size, Decimal("0"))

    if needs_packing:
        total += Decimal("2500")

    if needs_unpacking:
        total += Decimal("2000")

    return total