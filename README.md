# Philosophy Quotes

Live site: **https://ravi-kiran-agarthi.github.io/philosophy-quotes/**

Quote cards for Stoicism, Taoism, Zen Buddhism and Hindu philosophy. Each card has its own **New quote** button.

## Features

- 4 cards, 12 quotes each, random pick without immediate repeats
- Light / Dark / System theme; defaults to system, choice saved in `localStorage`, applied before paint (no flash)
- Nature green theme with high-contrast text, visible focus outlines, and `aria-live` quote updates
- Word of the Day card (no button): Merriam-Webster's free RSS feed, fetched at deploy time by `scripts/wotd.py` into `wotd.json`; the workflow redeploys daily at 06:15 UTC
- Fast on slow connections: ~9 KB `index.html`, inline CSS/JS, no dependencies or web fonts; only one tiny `wotd.json` request

## Development

No build step. Open `index.html` in a browser. Quotes live in the `Q` object in `index.html`.

## Deployment

Pushes to `main` deploy to GitHub Pages via `.github/workflows/pages.yml`.

## Note

Some Zen and Taoism entries are traditional sayings or proverbs rather than verified quotes; they are labelled accordingly.
