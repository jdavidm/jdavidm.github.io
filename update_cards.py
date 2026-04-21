import json
import difflib
from bs4 import BeautifulSoup

with open('aidelab_links.json', 'r') as f:
    aidelab_links = json.load(f)

# Create a flat dictionary mapping title to full URL
links_dict = {}
for title, href in aidelab_links:
    if href.startswith('http'):
        url = href
    else:
        url = "https://aidelab.arizona.edu" + href
    links_dict[title] = url

with open('publications.html', 'r') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.find_all('div', class_=lambda c: c and 'pub-card' in c)

for card in cards:
    title_tag = card.find(class_='pub-title')
    if not title_tag:
        continue

    title = title_tag.get_text(strip=True)

    # Clean up title for matching (remove trailing dots, newlines, etc)
    clean_title = title.replace('\n', ' ').strip('. ')

    # Try to find best match
    best_match = None
    best_ratio = 0

    for aidelab_title in links_dict.keys():
        clean_aidelab = aidelab_title.replace('\n', ' ').strip('. ')
        ratio = difflib.SequenceMatcher(None, clean_title.lower(), clean_aidelab.lower()).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = aidelab_title

    url = None
    if best_ratio > 0.75:
        url = links_dict[best_match]
        print(f"Matched '{title[:40]}...' to '{best_match[:40]}...' ({best_ratio:.2f}) -> {url}")
    else:
        # User requested the change for *all* cards on the publications page, not just those we found a direct link for. Let's create an implicit URL slug
        slug = title.lower()
        slug = __import__('re').sub(r'[^a-z0-9\s-]', '', slug)
        slug = __import__('re').sub(r'[\s-]+', '-', slug)
        slug = slug.strip('-')
        url = "https://aidelab.arizona.edu/" + slug
        print(f"Generated slug for '{title[:40]}...' -> {url}")

    # 1. Remove pub-links
    pub_links = card.find(class_='pub-links')
    if pub_links:
        pub_links.decompose()

    # 2. Change div to a
    card.name = 'a'
    card['href'] = url
    card['target'] = '_blank'
    card['rel'] = 'noopener noreferrer'

    # Handle style safely whether it exists or not
    existing_style = card.get('style', '')
    card['style'] = (existing_style + ' text-decoration: none; color: inherit; display: flex; flex-direction: column;').strip()

with open('publications.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Done updating publications.html")
