# news_fetcher.py

import feedparser
import datetime
import os

# Definieer een aantal RSS feeds voor ruimtevaartnieuws
feed_urls = {
    "NASA": "https://www.nasa.gov/rss/dyn/breaking_news.rss",
    "SpaceX": "https://www.spacex.com/news/rss-feed",  # Controleer of deze URL werkt
    "ESA": "https://www.esa.int/rssfeed",              # Pas indien nodig de URL aan
}

# Bouw de inhoud van het Markdown-bestand
markdown_content = "# Ruimtevaart Nieuws Update\n\n"
for source, url in feed_urls.items():
    d = feedparser.parse(url)
    markdown_content += f"## Source: {source}\n\n"
    # Haal bijvoorbeeld de drie nieuwste artikelen op
    for entry in d.entries[:3]:
        title = entry.title
        link = entry.link
        summary = entry.summary if hasattr(entry, "summary") else "Geen samenvatting beschikbaar."
        markdown_content += f"### [{title}]({link})\n"
        markdown_content += f"Summary: {summary}\n\n"
    markdown_content += "---\n\n"

# Creëer een bestandsnaam met datum en tijd
now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
directory = "reports"
if not os.path.exists(directory):
    os.makedirs(directory)
filename = os.path.join(directory, f"ruimtevaart_nieuws_report_{now}.md")

with open(filename, "w", encoding="utf-8") as f:
    f.write(markdown_content)

print(f"Nieuwsrapport opgeslagen als {filename}")

