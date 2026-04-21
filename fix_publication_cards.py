import re
import urllib.parse
from bs4 import BeautifulSoup

with open('publications.html', 'r') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.find_all('div', class_='pub-card')
print(f"Found {len(cards)} cards.")

def generate_slug(title):
    # Very basic slug generator
    title = title.lower()
    title = re.sub(r'[^a-z0-9\s-]', '', title)
    title = re.sub(r'[\s-]+', '-', title)
    return title.strip('-')

urls = []
for card in cards:
    title_el = card.find(class_='pub-title')
    if title_el:
        title = title_el.get_text(strip=True)
        # Custom mapping for the specific one requested
        if "Impact Evaluations" in title and "Data-Scarce" in title:
            slug = "impact-evaluations-data-poor-settings"
        elif "Food Without Fire" in title:
            slug = "food-without-fire"
        elif "Risk and Rainfall" in title:
            slug = "risk-and-rainfall-specification-sensitivity-estimating-smallholder-risk-preferences"
        else:
            slug = generate_slug(title)

        urls.append(slug)
        print(f"Title: {title[:50]}... -> Slug: {slug}")
