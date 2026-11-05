# Infonorm website

Statische website voor **Infonorm**, onafhankelijk IT- en energieadvies in
Noordwijkerhout. De site is gebouwd met [Astro](https://astro.build).

## Structuur

```text
src/
├── assets/                  Profielfoto (wordt door Astro geoptimaliseerd)
├── components/
│   ├── CallToAction.astro   Gedeelde donkere oproep onderaan pagina's
│   ├── CheckList.astro      Lijst met vinkjes
│   ├── ContactCard.astro    Contactkaart met e-mail en contactgegevens
│   ├── Footer.astro         Gedeelde footer
│   └── Header.astro         Navigatie en mobiel menu
├── data/site.ts             Site- en contactgegevens op één plek
├── layouts/BaseLayout.astro HTML-head, header, main en footer
├── pages/
│   ├── index.astro          Homepage
│   ├── diensten.astro       Diensten
│   ├── salderingsregeling.astro
│   ├── over-mij.astro       Over Friso
│   └── contact.astro        Contact
└── styles/global.css        Alle styling
public/
├── apple-touch-icon.png  Gegenereerd uit logo.svg (180×180)
├── favicon.ico           Gegenereerd uit logo.svg (48/32/16 px)
└── logo.svg              Het logo; wordt ook als favicon gebruikt
```

## Commands

```bash
npm install
npm run dev       # lokale ontwikkelserver op localhost:4321
npm run build     # productiebuild naar dist/
npm run preview   # bekijk de productiebuild lokaal
```

## Aanpassen

- **Contactgegevens, naam en locatie:** pas `src/data/site.ts` aan. Alle pagina's
  en componenten gebruiken deze waarden.
- **E-mailonderwerpen:** pas `emailLinks` in `src/data/site.ts` aan.
- **Navigatie:** pas `navItems` in `src/components/Header.astro` aan.
- **Footer:** pas `src/components/Footer.astro` aan.
- **Profielfoto:** vervang `src/assets/profielfoto_friso.png`.
- **Logo en favicon:** vervang `public/logo.svg`. De favicon verwijst rechtstreeks
  naar dit bestand; genereer daarna de overige iconen opnieuw:

  ```bash
  cd public
  magick -background none logo.svg -define icon:auto-resize=48,32,16 favicon.ico
  magick -background '#0d2a5c' logo.svg -flatten -resize 180x180 apple-touch-icon.png
  ```
- **Kleuren en typografie:** bovenaan `src/styles/global.css` bij `:root`.

Na een wijziging bouwt `npm run build` de volledige site opnieuw in `dist/`.
