# infonorm website

Eenvoudige statische website voor **infonorm**, IT-advies in Noordwijkerhout.
Geen frameworks: alleen HTML, CSS en een klein stukje JavaScript. De gedeelde
footer staat in één partial en wordt met een klein build-script in de pagina's
ingevoegd.

## Structuur

```
src/*.html                 Bronpagina's (met <!-- include: ... -->)
partials/footer.html       Gedeelde footer
build.py                   Bouwt src/ naar de HTML-bestanden in de root
index.html                 Homepage (gegenereerd)
diensten.html              Diensten (IT-advies, energiebeheer, automatisering)
salderingsregeling.html    Uitleg over het einde van de salderingsregeling (2027)
over-mij.html              Over Friso, met profielfoto
contact.html               Contactgegevens (info@infonorm.nl)
assets/css/style.css       Alle styling
assets/js/main.js          Mobiel menu en jaartal in de footer
assets/img/                Profielfoto en favicon
logo.svg                   Logo (header en footer)
promo_text.md              Brontekst voor de zonnepanelen-pagina
```

De HTML-bestanden in de root zijn de publiceerbare output. Pas inhoud aan in
`src/` en de footer in `partials/footer.html`, en draai daarna:

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

- **Footer:** pas `partials/footer.html` aan en draai `python3 build.py`.
- **E-mailadres:** `info@infonorm.nl` staat in de header/footer-links en op de
  contactpagina. Zoek en vervang het adres in `src/*.html` en
  `partials/footer.html`.
- **Telefoonnummer / WhatsApp:** nog niet ingevuld. Voeg dit toe aan
  `src/contact.html` (en eventueel `src/salderingsregeling.html`) zodra het
  bekend is.
- **Profielfoto:** vervang `assets/img/profielfoto_friso.png` door een nieuwe foto
  met dezelfde bestandsnaam, bij voorkeur portretformaat (3:4).
- **Logo:** vervang `logo.svg` door een nieuwe versie met dezelfde bestandsnaam.
- **LinkedIn:** de link naar `linkedin.com/in/friso-smit-884a19445` staat in de footer,
  op `src/over-mij.html` en op `src/contact.html`. Pas de URL en naam aan waar nodig.
- **Kleuren en typografie:** bovenaan `assets/css/style.css` bij `:root`.
- **Jaartal in de footer:** wordt automatisch bijgewerkt door `assets/js/main.js`.

## Publiceren

Draai eerst `python3 build.py` en zet daarna de gegenereerde HTML-bestanden in de
root samen met `assets/` en `logo.svg` in de webroot. Dat kan bijvoorbeeld via
GitHub Pages, Netlify of elke willekeurige webserver; `index.html` is de
startpagina.
