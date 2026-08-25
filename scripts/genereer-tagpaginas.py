#!/usr/bin/env python3
"""Genereert statische tagpagina's (/thema/<slug>/ en /niveau/<slug>/).

- Thema: één pagina per thema uit _data/tags.yml (vast vocabularium).
- Niveau: alleen pagina's voor niveauslugs die effectief in posts voorkomen,
  om lege ("thin content") pagina's te vermijden.

Draai dit script opnieuw (vanuit de repo-root) wanneer je een post tagt met
een niveau dat nog geen pagina heeft:  python3 scripts/genereer-tagpaginas.py
Bestaande pagina's worden overschreven; handmatige aanpassingen aan
stubpagina's gaan dus verloren (pas liever dit script aan).
"""
import glob
import io
import os

import yaml

NIVEAU_TITELS = {
    "basisonderwijs": "AI in het basisonderwijs",
    "kleuteronderwijs": "AI in het kleuteronderwijs",
    "lager-onderwijs": "AI in het lager onderwijs",
    "secundair-onderwijs": "AI in het secundair onderwijs",
    "eerste-graad": "AI in de eerste graad van het secundair",
    "tweede-graad": "AI in de tweede graad van het secundair",
    "derde-graad": "AI in de derde graad van het secundair",
    "hoger-onderwijs": "AI in het hoger onderwijs",
    "graduaat": "AI in het graduaat",
    "professionele-bachelor": "AI in de professionele bachelor",
    "academische-bachelor": "AI in de academische bachelor",
    "master": "AI in de master",
    "doctoraat-en-onderzoek": "AI in doctoraat en onderzoek",
    "levenslang-leren": "AI en levenslang leren",
    "volwassenenonderwijs": "AI in het volwassenenonderwijs",
    "deeltijds-kunstonderwijs": "AI in het deeltijds kunstonderwijs",
    "buitengewoon-onderwijs": "AI in het buitengewoon onderwijs",
    "lerarenopleiding": "AI in de lerarenopleiding",
}


def front_matter(pad):
    return yaml.safe_load(open(pad, encoding="utf-8").read().split("---")[2 - 1])


def gebruikte_niveaus():
    slugs = set()
    for p in glob.glob("_posts/*.md"):
        fm = front_matter(p)
        slugs.update(fm.get("niveau") or [])
    return slugs


def schrijf(dim, slug, fm):
    os.makedirs(dim, exist_ok=True)
    with io.open(f"{dim}/{slug}.md", "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.safe_dump(fm, f, allow_unicode=True, sort_keys=False,
                       default_flow_style=False, width=1000)
        f.write("---\n")


def main():
    tags = yaml.safe_load(open("_data/tags.yml", encoding="utf-8"))
    n = 0

    for t in tags["thema"]:
        slug, naam = t["slug"], t["naam"]
        naam_l = naam if slug.startswith("ai-") else naam.lower()
        schrijf("thema", slug, {
            "layout": "tag", "dim": "thema", "tag_slug": slug,
            "title": f"{naam} — AI en onderwijs",
            "h1": naam,
            "intro": (f"Alle artikels, onderzoek, beleid en media over {naam_l} "
                      "in de context van AI en onderwijs, in Vlaanderen en de wereld."),
            "description": (f"Artikels en onderzoek over {naam_l} rond AI in het "
                            "onderwijs — nieuws uit Vlaanderen en de wereld, "
                            "doorzoekbaar en geduid."),
            "permalink": f"/thema/{slug}/",
        })
        n += 1

    for slug in sorted(gebruikte_niveaus()):
        titel = NIVEAU_TITELS.get(slug)
        if not titel:
            print(f"!! niveau '{slug}' onbekend in NIVEAU_TITELS — overgeslagen")
            continue
        schrijf("niveau", slug, {
            "layout": "tag", "dim": "niveau", "tag_slug": slug,
            "title": titel,
            "h1": titel,
            "intro": (f"{titel}: nieuws, onderzoek, beleid en praktijkvoorbeelden "
                      "uit Vlaanderen en de wereld."),
            "description": (f"{titel}: nieuws, onderzoek, beleid en praktijkvoorbeelden "
                            "rond artificiële intelligentie, uit Vlaanderen en de wereld."),
            "permalink": f"/niveau/{slug}/",
        })
        n += 1

    print(f"{n} tagpagina's geschreven")


if __name__ == "__main__":
    main()
