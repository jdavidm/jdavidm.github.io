import re
import os
from pathlib import Path

mapping = {
    "11 - SICLC.png": "Socioeconomic Impacts of COVID-19 in Low-Income Countries",
    "12 - CFRTE.png": "Contract Farming and Rural Transformation",
    "13 - SFEED.png": "One Size Fits All?",
    "14 - REBSB.png": "Research Ethics Beyond the IRB",
    "15 - UPURU.jpg": "Ulysses' Pact or Ulysses' Raft",
    "17 - AGRIC.png": "Agriculture in the Process of Development",
    "19 - MMRYP.png": "Money Matters: The Role of Yields and Profits in Agricultural Technology Adoption",
    "20 - CONSE.png": "Conservation Agriculture and Climate Resilience",
    "22 - BFEAA.png": "Beasts of the Field? Ethics in Agricultural and Applied Economics",
    "24 - SDADP.png": "To Specialize or Diversify",
    "28 - RDIPA.png": "Risk, Crop Yields, and Weather Index Insurance in Village India",
    "3 - IEDEC.jpg": "Impact Evaluations in Data-Scarce Environments",
    "33 - VSSAR.png": "Valuing the Structural Sensitivities", # Let's guess for now, I'll use the codes for the ones not in mapping
    "34 - LCMEF.png": "Learning from a crisis",
    "4 - MWUEO.png": "The Mismeasure of Weather",
    "5 - FWFNE.png": "Food Without Fire",
    "6 - CHLDF.png": "Coping or Hoping",
    "7 - EUREO.png": "Expanding Undergraduate Research",
    "8 - PPMEI.png": "Privacy Protection",
    "9 - FIDFY.png": "Food Insecurity During the First Year",
}

def get_image_for_pub(title):
    images_dir = Path("/app/assets/images/publications")
    if not images_dir.exists():
        return ""

    for img_file in images_dir.iterdir():
        file_key = img_file.name
        if file_key in mapping:
            clean_title = title.lower()
            clean_map = mapping[file_key].lower()
            if clean_map in clean_title or clean_title in clean_map:
                return f"assets/images/publications/{img_file.name}"
            if clean_title.startswith(clean_map[:20]) or clean_map.startswith(clean_title[:20]):
                return f"assets/images/publications/{img_file.name}"

    # fallback to code match
    words = [w.capitalize() for w in re.findall(r'[a-zA-Z]+', title) if len(w) > 2]
    code = "".join(w[0] for w in words[:5]).upper()
    if len(code) < 5:
        code += "X" * (5 - len(code))

    for img in images_dir.iterdir():
        if code in img.name:
            return f"assets/images/publications/{img.name}"

    return ""

def parse_latex_pubs(tex_file):
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = {
        "book": r"\\item \{\\bf Books\}(.*?)\\item \{\\bf Journal Articles\}",
        "article": r"\\item \{\\bf Journal Articles\}(.*?)\\item \{\\bf Book Chapters\}",
        "chapter": r"\\item \{\\bf Book Chapters\}(.*?)\\item \{\\bf Working Papers, In Review, and In Prep\}",
        "working": r"\\item \{\\bf Working Papers, In Review, and In Prep\}(.*?)\\item \{\\bf Selected Non-Peer Reviewed Publications\}"
    }

    pubs = []

    for category, pattern in sections.items():
        match = re.search(pattern, content, re.DOTALL)
        if match:
            section_content = match.group(1)
            items = re.split(r'\\subitem(?:\[.*?\])?\s+', section_content)[1:]

            for item in items:
                item = item.strip()
                if not item or item.startswith('\\begin') or item.startswith('\\end'):
                    continue

                title = ""
                title_match = re.search(r"``(.*?)(?:''|')", item)
                if title_match:
                     title = title_match.group(1)
                else:
                     title_match = re.search(r'\\emph{(.*?)}', item)
                     if title_match:
                         title = title_match.group(1)

                title = re.sub(r'\\href{.*?}{(.*?)}', r'\1', title)
                title = title.replace('\\', '').replace('{', '').replace('}', '')

                if not title:
                     title = "Unknown Title"

                authors = ""
                journal = ""

                try:
                    parts = item.split(f"``") if "``" in item else item.split(r"\emph{")
                    authors_year = parts[0].strip()
                    authors = re.sub(r'\d{4}.*$', '', authors_year).strip()
                    if authors.endswith('.'): authors = authors[:-1]

                    authors = re.sub(r'\\', '', authors)
                    authors = authors.replace('"', '').replace('{', '').replace('}', '')

                    if len(parts) > 1:
                        after_title = parts[1].split("''")[-1] if "''" in parts[1] else parts[1].split("}")[-1]
                        journal_match = re.search(r'\\emph{(.*?)}', after_title)
                        if journal_match:
                            journal = journal_match.group(1)
                            year_match = re.search(r'(\d{4})', authors_year)
                            if year_match:
                                journal += f" ({year_match.group(1)})"
                        else:
                            if category == "working":
                                journal = "Working Paper / In Review"
                            elif category == "book":
                                journal = ""
                except Exception as e:
                    pass

                if not authors: authors = "Jeffrey D. Michler et al."

                journal = re.sub(r'\\href{.*?}{(.*?)}', r'\1', journal)
                journal = journal.replace('\\', '').replace('{', '').replace('}', '').strip()

                image_url = get_image_for_pub(title)

                links = []
                hrefs = re.findall(r'\\href{(.*?)}{(.*?)}', item)
                for url, text in hrefs:
                    if 'doi.org' in url or 'routledge.com' in url or 'nature.com' in url or 'aeaweb.org/articles' in url or 'aetr' in url or 'ageconsearch' in url:
                        links.append({"type": "published", "url": url, "text": "Published Version" if 'routledge' in url else "DOI" if 'doi' in url else "Link", "icon": "fa-link" if 'doi' in url else "fa-external-link-alt"})
                    elif 'arxiv' in url or 'ssrn' in url or 'documents.worldbank.org' in url or 'openknowledge.worldbank.org' in url or 'Working Paper' in text or 'Policy Research' in text:
                        links.append({"type": "preprint", "url": url, "text": "Working Paper", "icon": "fa-file-pdf"})
                    elif 'socialscienceregistry.org' in url or 'osf.io' in url:
                        links.append({"type": "pap", "url": url, "text": "Pre-analysis Plan", "icon": "fa-clipboard-check"})
                    elif 'github' in url or 'Replication' in text:
                        links.append({"type": "replication", "url": url, "text": "Replication Package", "icon": "fa-database"})

                pubs.append({
                    "category": category,
                    "title": title.strip(),
                    "authors": authors,
                    "journal": journal,
                    "image": image_url,
                    "links": links
                })

    return pubs

pubs = parse_latex_pubs('/app/michler_cv.tex')

# Write HTML to file
with open('pubs_html.txt', 'w') as f:
    for pub in pubs:
        cat_map = {
            "book": ("Book", "var(--color-accent)"),
            "article": ("Journal Article", "var(--color-primary-light)"),
            "chapter": ("Book Chapter", "var(--color-primary)"),
            "working": ("Working Paper", "#ca8a04")
        }
        tag_text, tag_color = cat_map.get(pub['category'], ("Publication", "var(--color-primary)"))

        has_image_class = "has-bg-image" if pub['image'] else ""
        bg_style = f"background: linear-gradient(to bottom, rgba(15, 23, 42, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%), url('{pub['image']}'); background-size: cover; background-position: center;" if pub['image'] else ""

        html = f'''
                <div class="pub-card {has_image_class}" data-category="{pub['category']}" style="{bg_style}">
                    <span class="card-tag" style="background-color: {tag_color}; color: white;">{tag_text}</span>
                    <h3 class="pub-title">{pub['title']}</h3>
                    <p class="pub-authors">{pub['authors']}</p>
                    <p class="pub-journal" style="font-weight: 500;">{pub['journal']}</p>
                    <div class="pub-links">'''

        for link in pub['links']:
            html += f'''
                        <a href="{link['url']}" target="_blank"><i class="fas {link['icon']}"></i> {link['text']}</a>'''

        html += '''
                    </div>
                </div>'''
        f.write(html + '\n')
