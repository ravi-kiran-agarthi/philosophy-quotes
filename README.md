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

Shows the same five philosophies with translated quotes (Stoicism: the 66 Gutenberg quotes; others: 12 each) into Telugu (no toggle). Translations are in `te.json`, loaded only in this mode, so the English page is unaffected. Word of the Day is hidden.

The Telugu translations are unreviewed; a native speaker should check nuance.

## Ask a meaning

Below Word of the Day: type or speak (mic, where the browser supports speech recognition) a word or saying, e.g. "what is reed?". Meanings come from the Datamuse API (no key), fetched only on submit, so page load is unaffected. English only.

## Update banner

The build SHA is stamped into `index.html` and `version.json` at deploy. The page checks `version.json` (no-store) every 5 min and on tab focus; if it differs, a "New changes available" bar with "Update now" shows. The button reloads via a fresh `?v=` URL, bypassing the HTTP cache. Fixed to the bottom so it causes no layout shift.
