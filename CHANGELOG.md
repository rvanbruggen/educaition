---
sitemap: false
---

# Changelog

Versienummer staat in `_config.yml` (`version`) en wordt getoond in de sitefooter,
samen met datum en uur van de laatste build (= laatste push naar `main`).

## 0.7.1 — 2026-08-25

- Leeshoek toegevoegd aan de Mediahoek (/media/): 13 boekposts (5 Nederlandstalig,
  8 internationaal) met nieuw type `boek` in het tagvocabularium.
- Goodreads-context bij boeken: nieuwe include `goodreads-badge.html` toont de
  gemiddelde score en het aantal beoordelingen als context (geen ranking), alleen
  bij ≥ 25 beoordelingen; anders enkel een reviewlink. Frontmatter-velden:
  `goodreads_url`, `goodreads_rating`, `goodreads_ratings`, `goodreads_checked`.
- Homepage: het Mediahoek-paneel toont nu naast de vier recentste podcasts ook de
  twee recentste boeken uit de Leeshoek (label "Uit de Leeshoek", met
  Goodreads-context) en linkt rechtstreeks naar /media/#leeshoek; boekposts
  worden uitgesloten van de Artikels-lijst (type `boek` toegevoegd aan de
  uitsluitlijst, zoals podcasts en digests).
- Mediahoek herschikt in twee kolommen (nieuwe `.media-grid`, naar het model van
  `.home-grid`): podcasts & vodcasts links (2/3), Leeshoek rechts (1/3), elk met
  Nederlandstalig/Internationaal; gestapeld op schermen smaller dan 900px.

## 0.7.0 — 2026-08-25

- SEO-verbeteringen (prioriteit 3 uit SEO-ACTION-PLAN.md):
  - 17 statische, crawlbare tagpagina's: `/thema/<slug>/` (alle 9 thema's) en
    `/niveau/<slug>/` (de 8 niveaus die in posts voorkomen — geen lege
    pagina's), via nieuwe layout `_layouts/tag.html`. Automatisch in de
    sitemap; elke pagina linkt naar alle andere tagpagina's en naar /filter/.
    Regenereren na het taggen met een nieuw niveau:
    `python3 scripts/genereer-tagpaginas.py`.
  - Niveau- en themabadges op postpagina's zijn nu links naar die tagpagina's
    (`tag-badges.html` met `links=true`; homepage-badges blijven JS-filters).
  - "Lees ook"-blok op postpagina's: max. vier verwante artikels met een
    gedeeld thema.
  - FAQPage JSON-LD (schema.org) op /faq/, automatisch opgebouwd uit de
    details/summary-blokken.
  - Crawlbare "Blader per thema / onderwijsniveau"-links onderaan /filter/.

## 0.6.7 — 2026-08-25

- SEO-verbeteringen (prioriteit 2 uit SEO-ACTION-PLAN.md):
  - Homepagina-titel nu trefwoordrijk ("AI en onderwijs in Vlaanderen — nieuws,
    onderzoek en beleid") in plaats van "Home".
  - `lang: nl_BE` zodat og:locale correct is; `author`, `logo` en `social`
    toegevoegd voor volledige JSON-LD.
  - Standaard social share-afbeelding (`assets/img/og-default.png`, 1200×630)
    voor alle pagina's zonder eigen beeld; PNG-logo (`logo-512.png`) toegevoegd.
  - `/CHANGELOG/` uit de sitemap gehaald (`sitemap: false`).
  - Handgeschreven meta descriptions voor de vier digestposts.

## 0.6.6 — 2026-08-24

- Volledige eerste zin als fragment nu ook op de artikels-, academisch-, media-
  en digestpagina's — de logica staat in één gedeelde include
  (`_includes/eerste-zin.html`), die ook de homepage en search.json gebruiken;
  geen afgekapte halve zinnen meer waar dan ook

## 0.6.5 — 2026-08-24

- Fix: ook search.json wordt nu met een versieparameter geladen op de
  artikelspagina, zodat zoekdata (incl. thumbnails) na een release niet uit een
  verouderde browsercache komt

## 0.6.4 — 2026-08-24

- Artikelspagina (/filter/): zoekresultaten tonen nu dezelfde OG-thumbnails als
  de homepage — `image`-veld toegevoegd aan search.json, weergave in de
  resultatenlijst met dezelfde stijl en stille fallback

## 0.6.3 — 2026-08-24

- Fix: woorden in artikelfragmenten plakten aan elkaar wanneer de brontekst een
  regeleinde bevatte ("hetlerarenplatform") — `normalize_whitespace` in plaats
  van `strip_newlines`

## 0.6.2 — 2026-08-24

- Homepage: maximaal 15 artikels in de lijst
- Artikelkaarten: het fragment is nu de volledige eerste zin van de post — geen
  afgekapte halve zinnen of woorden meer
- De intropagraaf loopt over de volledige paginabreedte

## 0.6.1 — 2026-08-24

- Fix: de stylesheet wordt nu geladen met een versieparameter
  (`style.css?v=<versie>`) zodat browsers na elke release de nieuwe CSS ophalen —
  bezoekers met een gecachete oude stylesheet zagen de artikelthumbnails op
  natuurlijke grootte, wat de homepage-layout brak
- Artikelthumbnails: uniforme grootte, relatief aan de pagina — maximaal 15% van
  de schermbreedte (clamp 120-216px), 16:9 bijgesneden

## 0.6.0 — 2026-08-24

- Homepage visueler: artikelkaarten tonen nu een thumbnail — het Open
  Graph-beeld van het bronartikel, rechtstreeks gehotlinkt (geen kopieën in de
  repo), lazy-loaded, zonder referrer, en met stille fallback als een beeld
  ontbreekt of verdwijnt; 26 bestaande posts kregen een `image:`-veld en de
  dagelijkse artikeltaak neemt het veld voortaan automatisch mee
- Nieuw mediapaneel in de rechterkolom: de vier recentste podcast-/vodcastposts
  met ingebedde Spotify-/YouTube-spelers, onder het digestpaneel
- Digestpaneel niet langer sticky (er staan nu twee panelen in de kolom)

## 0.5.4 — 2026-08-24

- Herpositionering: de site presenteert zich voortaan als "dé hub voor AI en
  onderwijs in Vlaanderen en de wereld" in plaats van als wekelijkse samenvatting —
  nieuwe kop en uitgebreidere intro op de homepage, aangepaste meta-description
  (`_config.yml`), README en Over-pagina
- Over-pagina: legt nu uit hoe de site evolueerde van wekelijkse nieuwssamenvatting
  naar verzamelpunt voor artikels, academisch onderzoek, media en regelgeving

## 0.5.3 — 2026-08-24

- Homepage: themakiezer onder de kop "Artikels" — klikbare pills filteren de
  artikellijst ter plekke, met teller; ook de pills op de artikelkaarten zelf zijn
  nu selecteerbaar als filter
- "Verkennen" heet voortaan "Artikels" (nav en paginatitel); de URL `/filter/`
  blijft ongewijzigd, dus geen gebroken links
- Artikelspagina: de badges in de zoekresultaten krijgen nu dezelfde kleuren per
  facet (niveau, vak, thema, regio, type) als op de homepage

## 0.5.2 — 2026-08-24

- Samengevat: dubbele week 34-edities opgeruimd — de digesttaak liep tweemaal,
  waardoor er per markt twee posts met dezelfde slug bestonden (URL-conflict op
  `/2026/08/digest-week-34/` en `/2026/08/digest-internationaal-week-34/`)
- Vlaanderen: de editie van 19/08 verwijderd; haar drie items zitten integraal in
  "Samengevat, week 34" van 23/08
- Internationaal: de vier items van 19/08 (Ohio, STUDENTS FIRST Act, VK-cijfers,
  EU-OESO AI-geletterdheidskader) samengevoegd in de editie van 23/08 als items 5-8;
  de post van 19/08 verwijderd — geen inhoud verloren

## 0.5.1 — 2026-08-24

- Mediahoek: ingebedde spelers — Spotify-showspelers en privacyvriendelijke
  YouTube-embeds (youtube-nocookie.com) via nieuwe front-matterattributen
  `spotify_show`, `spotify_episode` en `youtube_id`; spelers verschijnen op de
  postpagina én inline op /media/ (nieuwe include `embed-player.html`, lazy loading)
- Mediahoek: dubbele vermelding samengevoegd — "AI en Onderwijs" en "Onderwijs & AI
  (Metis)" bleken dezelfde podcast van Metis Onderwijsadvies te zijn; één post blijft
  over, met hosts en alle luisterlinks
- Opmerking: de wijzigingen aan include/layout/CSS werden op 2026-08-23 al
  meegecommit door een geplande taak (commit "New run")

## 0.5.0 — 2026-08-22

- Nieuwe sectie "Academische hoek" (`/academisch/`): Nederlandstalige samenvattingen
  van wetenschappelijk onderzoek over AI in het onderwijs (nieuw posttype
  `academische-publicatie`), met zes startpublicaties
- Nieuwe sectie "Mediahoek" (`/media/`): podcasts en vodcasts over AI in het
  onderwijs, Nederlandstalig en internationaal (nieuw posttype `podcast-vodcast`),
  met tien startitems
- "Digest" heet overal op de site voortaan "Samengevat" (nav, homepage, pagina- en
  filterlabels); URL's en tag-slugs blijven ongewijzigd, dus geen gebroken links
- Homepage: academische en mediaposts verschijnen niet in de artikellijst — ze
  hebben hun eigen secties
- Git: credential helper gebruikt nu een relatief pad, zodat pushes uit elke
  sessie werken

## 0.4.2 — 2026-08-20

- Fix: `url`/`baseurl` in `_config.yml` stonden nog op de oude GitHub Pages
  project-URL (`rvanbruggen.github.io/educaition`) i.p.v. het eigen domein —
  alle interne links, afbeeldingen en de canonical/OG-tags gaven 404's op
  `www.educaition.today`
- `url` staat nu op `https://www.educaition.today`, `baseurl` is leeg

## 0.4.1 — 2026-08-19

- Mobiel: hamburgermenu in de header (CSS-only, werkt zonder JavaScript) —
  navigatie en zoekbalk klappen open/dicht op schermen tot 768px
- Verkennen: "Alle digests"-optie in de Type-filter (matcht Vlaamse én
  internationale digests)

## 0.4.0 — 2026-08-19

- Homepage: gebruikt nu 90% van de schermbreedte (header en footer ook)
- Homepage: tweekolomslayout — artikels links, digests rechts in een eigen
  gekleurd paneel (sticky), met labels Vlaanderen/Internationaal per digest
- Internationale digest toegevoegd (week 34) + type `digest-internationaal`;
  digestpagina gegroepeerd per soort
- Wekelijkse geplande taak: elke zondag 18:00 onderzoek + draft van beide digests

## 0.3.1 — 2026-08-19

- Fix: interne links in de digest misten de baseurl-prefix (`post_url` voegt die
  niet zelf toe op Jekyll 3.x) en gaven 404's
- Preventie: GitHub Action toegevoegd die bij elke push de site bouwt en alle
  interne links controleert (html-proofer); redactieregel toegevoegd aan README
- README en Over-pagina: link naar de live site en feedbackprocedure (issues/PR's)

## 0.3.0 — 2026-08-19

- Volledige-tekstzoekfunctie: zoekbalk in de header (gaat naar `/filter/?q=…`) en
  live zoeken op de Verkennen-pagina, gecombineerd met de facetfilters
- Zoekindex uitgebreid met de volledige artikeltekst (`search.json`)
- Zoektermen worden gemarkeerd in de resultaten; zoekopdracht zit in de URL en is deelbaar
- "Ter discussie": duidelijkere visuele scheiding per debat (genummerde, gekleurde blokken + index)
- Logo: datalijnen toegevoegd op de rechterpagina van het boek

## 0.2.0 — 2026-08-19

- FAQ toegevoegd (drie perspectieven: lerenden, leerkrachten, directies), volledig gesourced
- "Ter discussie"-sectie toegevoegd: open vragen met standpunten en bronnen, zonder antwoorden (`_data/discussies.yml`)
- Versionering: versienummer + laatst-bijgewerkt-timestamp in de footer
- Nieuwe look & feel: logo, typografie (Fraunces/Inter), warmer kleurenpalet

## 0.1.0 — 2026-08-19

- Eerste scaffold: Jekyll-site met zes-facettaxonomie (`_data/tags.yml`)
- Client-side facetfilter (`filter.html` + `search.json`)
- Wekelijkse digest-structuur en vier eerste artikels
- Fix: `baseurl` voor GitHub Pages project page
