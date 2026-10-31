"""Fetch Merriam-Webster Word of the Day RSS and write a small JSON file."""
import html, json, re, sys, urllib.request

FEED = "https://www.merriam-webster.com/wotd/feed/rss2"
req = urllib.request.Request(FEED, headers={"User-Agent": "philosophy-quotes-site"})
xml = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
item = xml[xml.index("<item>"):]


def cdata(tag):
    m = re.search(r"<%s><!\[CDATA\[(.*?)\]\]></%s>" % (tag, tag), item, re.S)
    return m.group(1) if m else ""


def text(s):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", "", s)).split())


desc = cdata("description")
head = re.search(r"<strong>([^<]+)</strong>\s*&#149;\s*\\([^\\]*)\\\s*&nbsp;\s*&#149;\s*<em>([^<]+)</em>", desc)
body = re.search(r"<br />\s*<p>(.*?)</p>", desc, re.S)
ex = re.search(r"<p>//\s*(.*?)</p>", desc, re.S)
if not (head and body):
    sys.exit("feed format changed")

out = {
    "word": text(head.group(1)),
    "pron": text(head.group(2)),
    "pos": text(head.group(3)),
    "def": text(body.group(1)),
    "ex": text(ex.group(1)) if ex else "",
    "url": cdata("link"),
}
with open(sys.argv[1], "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
print(out)
