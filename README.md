# Philosophy Quotes

Live site: **https://ravi-kiran-agarthi.github.io/philosophy-quotes/**

Quote cards for Stoicism, Taoism, Zen Buddhism, Hindu and Christian philosophy. Each card has its own **New quote** button.

## Features

- 5 cards (Stoicism, Taoism, Zen, Hindu, Christian), 12 quotes each, random pick without immediate repeats
- Light / Dark / System theme (picker uses customizable `appearance: base-select` where supported, native select elsewhere), with an emoji icon per option; defaults to system, choice saved in `localStorage`, applied before paint (no flash)
- Nature green theme with high-contrast text, visible focus outlines, and `aria-live` quote updates
- Word of the Day section below the cards (no button, no card): Merriam-Webster's free RSS feed, fetched at deploy time by `scripts/wotd.py` into `wotd.json`; the workflow redeploys daily at 06:15 UTC; pronunciation clip (~5 KB) loads only when "Listen" is pressed
- Fast on slow connections: ~9 KB `index.html`, inline CSS/JS, no dependencies or web fonts; only one tiny `wotd.json` request

## Development

No build step. Open `index.html` in a browser. Quotes live in the `Q` object in `index.html`.

## Deployment

Pushes to `main` deploy to GitHub Pages via `.github/workflows/pages.yml`.

## Note

Some entries (Zen, Taoism, and a few attributed to Augustine or Aquinas) are traditional sayings or attributions rather than verified quotes; they are labelled accordingly.

## Telugu

Open `?lang=te`: https://ravi-kiran-agarthi.github.io/philosophy-quotes/?lang=te

Shows Telugu cards instead of the English ones (no toggle). Verses are loaded from `te.json` only in this mode, so the English page is unaffected. Word of the Day is hidden.

- **Vemana**: verses from *Vemana Padyalu* (17th century, C. P. Brown 1910 edition)
- **Bhagavad Gita**: *Andhra Bhagavad Gita* by Tadoori Lakshmi Narasimha Rayakavi (1911)

Both are public-domain texts, used verse-only (original verses, no modern translations or commentary). Verses were selected from Telugu Wikisource and are not edited; their wording may include old spellings or transcription errors.
