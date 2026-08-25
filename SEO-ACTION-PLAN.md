# SEO action plan — www.educaition.today

*Audit date: 25 August 2026. Based on the live site (v0.6.6) and this repo.*

## What is already in good shape

The technical foundation is solid. The site uses `jekyll-seo-tag`, `jekyll-sitemap` and `jekyll-feed`: every page gets a canonical URL, Open Graph and Twitter Card tags, and JSON-LD structured data. A `robots.txt` with a sitemap reference and a complete `sitemap.xml` (63 URLs) are served correctly. The apex domain `educaition.today` 301-redirects to `www`, permalinks are clean (`/2026/08/slug/`), post pages get a meta description from the first paragraph automatically, and the site is fast, mobile-friendly static HTML. Nothing blocks crawling.

## Priority 1 — Get indexed (do this first)

The site appears not to be in Google's index yet (`site:educaition.today` returns nothing). The domain went live around 20 August, so this is expected — but it will not fix itself quickly for a brand-new domain.

1. **Register the site in Google Search Console** (google.com/webmasters). Use a "Domain" property, verified via a DNS TXT record at your registrar. Then submit `https://www.educaition.today/sitemap.xml` and use "URL inspection → Request indexing" on the homepage and the key pages (/filter/, /digest/, /faq/, /over/).
2. **Register in Bing Webmaster Tools** too — it feeds DuckDuckGo and Ecosia (popular in education), and you can import the property from Search Console in one click.
3. Check back in Search Console after ~1 week for coverage errors.

## Priority 2 — Quick on-page fixes in this repo (an hour of work)

4. **Homepage title.** It currently renders as "Home | EducAItion" — the single most important title on the site carries no keywords. In `index.html`, change `title: Home` to something like `title: "AI en onderwijs in Vlaanderen — nieuws, onderzoek en beleid"`.
5. **Set a proper locale.** `og:locale` renders as `nl`; add `locale: nl_BE` to `_config.yml` (jekyll-seo-tag picks it up).
6. **Add a default social image.** Posts without an `image` (and all overview pages) have no `og:image`. Add a branded 1200×630 image to `assets/img/` and set it as the seo-tag default (`defaults` → `image`) in `_config.yml`. Also add `logo:` and `social:` (name + links) to `_config.yml` so the JSON-LD Organization block is complete.
7. **Keep CHANGELOG out of the sitemap.** `https://www.educaition.today/CHANGELOG/` is listed; add `sitemap: false` front matter to it (or move it out of the published site).
8. **Post descriptions.** None of the 54 posts have a `description:` front matter field; the auto-excerpt works well because your first paragraphs are strong, so this is optional — but for the digests (long-form, your most valuable pages) a hand-written description is worth it.

## Priority 3 — Structural improvements (the biggest ranking lever on-site)

9. **Create static, crawlable tag/theme pages.** The `/filter/` page is entirely JavaScript-driven, so search engines see no landing page for themes like "AI-geletterdheid", "Evaluatie & fraude" or levels like "Secundair onderwijs". These are exactly the phrases teachers search for. Generate one static page per thema and per niveau (a simple loop over `_data/tags.yml`, one small HTML file per tag with the filtered post list — no plugin needed, GitHub Pages-safe), link them from the badges, and let the sitemap pick them up. This is the highest-impact content change you can make.
10. **FAQ rich results.** `faq.html` has ~18 Q&A blocks; add `FAQPage` JSON-LD so Google can show it as a rich result.
11. **Internal linking.** Posts currently link out to the source but rarely to each other. Add a "related articles" block on post pages (match on shared thema tags) and link from digest entries to the underlying posts and back. This spreads authority and keeps crawlers moving.
12. **Self-host key images.** Thumbnails and `og:image` values hotlink to VRT, Veto, VAIA etc. — these can disappear or block hotlinking, and they're invisible to Google Images as *your* content. At minimum rely on the default social image (point 6); ideally store an own copy for evergreen pages. Also give thumbnails a meaningful `alt` (currently `alt=""`).

## Priority 4 — Authority building (the real driver for a new domain)

13. **Earn backlinks from the Flemish education ecosystem.** A new domain ranks on links, not on-page polish. Concrete targets: a KlasCement listing (websites section), Mediawijs, Schoolmakers, VAIA, onderwijs-nieuwsbrieven, and the organisations you cover — when you summarise their work, tell them; many will link back. One good link from klascement.net is worth more than everything in Priority 2.
14. **Publish the weekly digest on LinkedIn** with a canonical link back to the site — your network is the fastest distribution channel you have, and consistent traffic signals help.
15. **Monitor.** Search Console (coverage + queries) weekly; Cloudflare Analytics is already installed for traffic.

## One thing to keep an eye on

During the audit, `www.educaition.today/` briefly served an older build (v0.5.3, old homepage copy) while other pages served v0.6.6 — most likely GitHub Pages CDN cache from last night's deploy. If you see stale content after future deploys, verify with a hard refresh and check the Pages build status.

---

*Sources: live checks of https://www.educaition.today/ (homepage, robots.txt, sitemap.xml, post pages) and the repo files `_config.yml`, `_layouts/default.html`, `_layouts/post.html`, `index.html`, `filter.html`, `faq.html`, `_posts/` (54 files, 0 with `description:`).*
