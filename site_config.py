"""Centrale plek voor de gegevens van de website.

Pas hier de contactgegevens, naam en locatie aan. ``build.py`` vervangt de
placeholders in ``src/*.html`` en ``partials/*.html`` door de waarden uit
``VARIABLES``. Gebruik in de HTML bijvoorbeeld ``{{ email }}`` of
``{{ email_url_advice }}``.

Een onbekende placeholder laat de build bewust falen, zo merk je meteen een
typefout.
"""

from urllib.parse import quote

# --- Basisgegevens ---------------------------------------------------------

SITE_NAME = "Infonorm"
OWNER_NAME = "Friso Smit"
OWNER_FIRST_NAME = "Friso"

EMAIL = "info@infonorm.nl"
DOMAIN = "infonorm.nl"

CITY = "Noordwijkerhout"
COUNTRY = "Nederland"

# Nog geen telefoonnummer bekend. Vul hier het nummer in (bijvoorbeeld
# "+31 6 12345678") en gebruik {{ phone }} / {{ phone_url }} in de HTML.
PHONE = ""

LINKEDIN_URL = "https://www.linkedin.com/in/friso-smit-884a19445/"
LINKEDIN_LABEL = OWNER_NAME

WHATSAPP = "Op aanvraag via e-mail"
RESPONSE_TIME = "Meestal binnen één werkdag"


# --- Afgeleide waarden -----------------------------------------------------

def mailto(subject: str = "") -> str:
    """Bouw een mailto-link, met optioneel een URL-encoded onderwerp."""
    url = f"mailto:{EMAIL}"
    if subject:
        url += "?subject=" + quote(subject, safe="")
    return url


VARIABLES = {
    # Namen en merk
    "site_name": SITE_NAME,
    "owner_name": OWNER_NAME,
    "owner_first_name": OWNER_FIRST_NAME,
    # E-mail
    "email": EMAIL,
    "email_url": mailto(),
    "email_url_advice": mailto(f"Adviesaanvraag via {DOMAIN}"),
    "email_url_solar": mailto("Gratis adviesgesprek zonnepanelen"),
    # Locatie
    "city": CITY,
    "country": COUNTRY,
    "location": f"{CITY}, {COUNTRY}",
    "service_area": f"{CITY} en omgeving",
    "service_area_or": f"{CITY} of omgeving",
    # Overig contact
    "phone": PHONE,
    "phone_url": f"tel:{PHONE.replace(' ', '')}" if PHONE else "",
    "whatsapp": WHATSAPP,
    "response_time": RESPONSE_TIME,
    "linkedin_url": LINKEDIN_URL,
    "linkedin_label": LINKEDIN_LABEL,
    "domain": DOMAIN,
}
