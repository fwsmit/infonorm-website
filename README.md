# Infonorm website

Eenvoudige statische website voor **Infonorm**, IT-advies in Noordwijkerhout.
Geen frameworks: alleen HTML, CSS en een klein stukje JavaScript. De gedeelde
footer staat in één partial en wordt met een klein build-script in de pagina's
ingevoegd.

## Structuur

```
src/*.html                 Bronpagina's (met <!-- include: ... -->)
partials/footer.html       Gedeelde footer
site_config.py             Alle site- en contactgegevens (één plek)
build.py                   Bouwt src/ naar de HTML-bestanden in de root
index.html                 Homepage (gegenereerd)
diensten.html              Diensten (IT-advies, energiebeheer, automatisering)
salderingsregeling.html    Uitleg over het einde van de salderingsregeling (2027)
over-mij.html              Over Friso, met profielfoto
contact.html               Contactgegevens (gegenereerd)
assets/css/style.css       Alle styling
assets/js/main.js          Mobiel menu en jaartal in de footer
assets/img/                Profielfoto en favicon
logo.svg                   Logo (header en footer)
promo_text.md              Brontekst voor de zonnepanelen-pagina
```

De HTML-bestanden in de root zijn de publiceerbare output en worden bij elke
build opnieuw geschreven; bewerk die dus niet met de hand. Pas inhoud aan in
`src/` en de footer in `partials/footer.html`, wijzig contactgegevens in
`site_config.py`, en draai daarna:

```bash
python3 build.py
```

## Lokaal bekijken

Open `index.html` direct in de browser, of start een kleine webserver:

```bash
python3 -m http.server 8000
```

en ga naar <http://localhost:8000>.

## Aanpassen

- **Contactgegevens, naam en locatie:** pas `site_config.py` aan en draai
  `python3 build.py`. E-mailadres, plaats, LinkedIn-URL en reactietijd staan daar
  één keer; de pagina's gebruiken placeholders zoals `{{ email }}`,
  `{{ email_url }}`, `{{ city }}` en `{{ linkedin_url }}`.
- **Telefoonnummer / WhatsApp:** vul `PHONE` (en eventueel `WHATSAPP`) in
  `site_config.py` in. `{{ phone }}` en `{{ phone_url }}` zijn dan direct in de
  HTML te gebruiken.
- **Footer:** pas `partials/footer.html` aan en draai `python3 build.py`.
- **Profielfoto:** vervang `assets/img/profielfoto_friso.png` door een nieuwe foto
  met dezelfde bestandsnaam, bij voorkeur portretformaat (3:4).
- **Logo:** vervang `logo.svg` door een nieuwe versie met dezelfde bestandsnaam.
- **Kleuren en typografie:** bovenaan `assets/css/style.css` bij `:root`.
- **Jaartal in de footer:** wordt automatisch bijgewerkt door `assets/js/main.js`.

Een onbekende placeholder (bijvoorbeeld `{{ emial }}`) laat de build met een
duidelijke foutmelding stoppen.

De e-mailvariabele staat alleen als waarde in `site_config.py`. In `src/` en
`partials/` staat nergens meer het adres zelf. De gegenereerde HTML-bestanden in
de root bevatten het ingevulde adres wél, omdat een statische site nu eenmaal
definitieve HTML nodig heeft. Wijzig je het adres, dan werkt één aanpassing in
`site_config.py` plus `python3 build.py` door op alle pagina's.

## Publiceren

Draai eerst `python3 build.py` en zet daarna de gegenereerde HTML-bestanden in de
root samen met `assets/` en `logo.svg` in de webroot. Dat kan bijvoorbeeld via
GitHub Pages, Netlify of elke willekeurige webserver; `index.html` is de
startpagina.
