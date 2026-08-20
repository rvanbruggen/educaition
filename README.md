# EducAItion

AI en onderwijs in Vlaanderen — nieuws, best practices en regelgeving, wekelijks
samengevat en doorzoekbaar per niveau, vak, thema en regio.

**Live site:** [https://www.educaition.today](https://www.educaition.today)
*(voorheen [https://rvanbruggen.github.io/educaition/](https://rvanbruggen.github.io/educaition/); sinds v0.4.2 draait de site op het eigen domein, `url`/`baseurl` in `_config.yml` zijn hierop aangepast)*

Statische site, gebouwd met Jekyll en gehost op GitHub Pages. Geen backend, geen database.

## Vragen, opmerkingen of suggesties

Zoals vermeld op de [Over-pagina](https://www.educaition.today/over/) verloopt
feedback via GitHub:

- **Vragen of opmerkingen** over de inhoud van de site: open een
  [issue](https://github.com/rvanbruggen/educaition/issues) in deze repository.
- **Concrete verbeteringen** (een correctie, een nieuwe bron, een extra artikel,
  een nieuwe discussievraag): fork de repo en dien een
  [pull request](https://github.com/rvanbruggen/educaition/pulls) in. Gebruik daarbij
  alleen tags die in `_data/tags.yml` staan en vermeld altijd je bronnen.

## Structuur

- `_config.yml` — sitesetup (GitHub Pages-veilige plugins: feed, seo-tag, sitemap)
- `_data/tags.yml` — het gecontroleerde tagvocabularium (zes facetten: niveau, vak, thema, regio, type, doelgroep). Nieuwe tags alleen via dit bestand.
- `_posts/` — alle artikels en digests, markdown met facet-front-matter
- `filter.html` + `search.json` — client-side facetfilter, geen server nodig
- `digest.html` — overzicht van wekelijkse digests (posts met `type: digest`)

## Nieuw artikel toevoegen

Maak `_posts/JJJJ-MM-DD-titel.md` met front matter:

```yaml
---
title: "Titel"
date: 2026-08-19
niveau: [secundair-onderwijs]
vak: [vakoverschrijdend]
thema: [beleid-en-regelgeving]
regio: [vlaanderen]
type: nieuws
doelgroep: [leerkracht]
bron: https://...
---
```

Gebruik alleen slugs die in `_data/tags.yml` staan.

**Interne links in artikels:** gebruik altijd
`[tekst]({{ site.baseurl }}{% post_url JJJJ-MM-DD-titel %})` — dus mét
`{{ site.baseurl }}` ervoor. Sinds v0.4.2 (eigen domein) staat `baseurl` leeg
in `_config.yml`, dus de prefix lost op naar niets — maar de link blijft
correct en toekomstbestendig als `baseurl` ooit weer een waarde krijgt.
De GitHub Action `check-links.yml` bouwt de site bij elke push en faalt op
kapotte interne links, zodat dit niet meer onopgemerkt live kan gaan.

## Lokaal draaien

```bash
bundle install
bundle exec jekyll serve
```

## Publiceren

Push naar `main` en activeer GitHub Pages (Settings → Pages → Deploy from branch → `main`).
