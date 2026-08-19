# Changelog

Versienummer staat in `_config.yml` (`version`) en wordt getoond in de sitefooter,
samen met datum en uur van de laatste build (= laatste push naar `main`).

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
