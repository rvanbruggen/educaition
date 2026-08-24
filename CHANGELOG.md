# Changelog

Versienummer staat in `_config.yml` (`version`) en wordt getoond in de sitefooter,
samen met datum en uur van de laatste build (= laatste push naar `main`).

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
