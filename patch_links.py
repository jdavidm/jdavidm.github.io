import re
import os

files = ['/app/index.html', '/app/cv.html', '/app/publications.html', '/app/teaching.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # We don't have his exact GS ID from the tex, but usually we can search it, wait, let me just fix the link to a general search if we don't have it, or use his actual ID if I can find it.
    # Let me use the search URL if we can't find the exact ID.
    scholar_url = "https://scholar.google.com/scholar?q=Jeffrey+D.+Michler"
    content = re.sub(r'https://scholar\.google\.com/citations\?user=your_id_here', scholar_url, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
