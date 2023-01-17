"This module contains currency convertion functions"

RATES = {"USDEUR": 0.85, "GBPEUR": 1.13, "CHFEUR": 0.86, "EURGBP": 0.885}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    if currency not in ["EUR", "USD", "GBP", "CHF"]:
        return None
    if currency == "EUR":
        if amount[1] == "EUR":
            # round the value with no decimal places
            return round(amount[0])
        if amount[1] == "USD":
            return round(amount[0] * RATES["USDEUR"])
        if amount[1] == "GBP":
            return round(amount[0] * RATES["GBPEUR"])
        if amount[1] == "CHF":
            return round(amount[0] * RATES["CHFEUR"])
    if currency == "GBP":
        if amount[1] == "EUR":
            return round(amount[0] * RATES["EURGBP"])
