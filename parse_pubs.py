import re
import json
import os

def parse_latex_pubs(tex_file):
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find sections
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
            # Split by \subitem
            items = re.split(r'\\subitem(?:\[.*?\])?\s+', section_content)[1:]

            for item in items:
                item = item.strip()
                if not item or item.startswith('\\begin') or item.startswith('\\end'):
                    continue

                # Try to extract title
                title = ""
                title_match = re.search(r'``(.*?)\'\'', item)
                if title_match:
                     title = title_match.group(1)
                else:
                     title_match = re.search(r'\\emph{(.*?)}', item)
                     if title_match:
                         title = title_match.group(1)

                if not title:
                     title = "Unknown Title"

                # Generate code for matching image
                words = [w.capitalize() for w in re.findall(r'[a-zA-Z]+', title) if len(w) > 2]
                code = "".join(w[0] for w in words[:5]).upper()
                if len(code) < 5:
                     code += "X" * (5 - len(code))


                # Links extraction
                links = []
                # Find all hrefs
                hrefs = re.findall(r'\\href{(.*?)}{(.*?)}', item)
                for url, text in hrefs:
                    if 'doi.org' in url or 'routledge.com' in url or 'nature.com' in url or 'aeaweb.org/articles' in url or 'aetr' in url or 'ageconsearch' in url:
                        links.append({"type": "published", "url": url, "text": "Published Version" if 'routledge' in url else "DOI" if 'doi' in url else "Link"})
                    elif 'arxiv' in url or 'ssrn' in url or 'documents.worldbank.org' in url or 'openknowledge.worldbank.org' in url or 'Working Paper' in text:
                        links.append({"type": "preprint", "url": url, "text": "Working Paper"})
                    elif 'socialscienceregistry.org' in url or 'osf.io' in url:
                        links.append({"type": "pap", "url": url, "text": "Pre-analysis Plan"})
                    elif 'github' in url or 'Replication' in text:
                        links.append({"type": "replication", "url": url, "text": "Replication Package"})

                pubs.append({
                    "category": category,
                    "title": title,
                    "code": code,
                    "links": links,
                    "raw": item
                })

    return pubs

print(json.dumps(parse_latex_pubs('/app/michler_cv.tex'), indent=2))
