# EducAItion

AI en onderwijs in Vlaanderen — nieuws, best practices en regelgeving, wekelijks
samengevat en doorzoekbaar per niveau, vak, thema en regio.

Statische site, gebouwd met Jekyll en gehost op GitHub Pages. Geen backend, geen database.

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

## Lokaal draaien

```bash
bundle install
bundle exec jekyll serve
```

## Publiceren

Push naar `main` en activeer GitHub Pages (Settings → Pages → Deploy from branch → `main`).
