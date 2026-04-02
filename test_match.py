import re
from pathlib import Path

def get_image_for_pub(title):
    words = [w.capitalize() for w in re.findall(r'[a-zA-Z]+', title) if len(w) > 2]
    code = "".join(w[0] for w in words[:5]).upper()
    if len(code) < 5:
        code += "X" * (5 - len(code))

    print(f"Title: {title}")
    print(f"Code: {code}")

    images_dir = Path("/app/assets/images/publications")
    if not images_dir.exists():
        return ""

    for img in images_dir.iterdir():
        if code in img.name:
            print(f" MATCHED: {img.name}")
            return f"assets/images/publications/{img.name}"

    print(" NO MATCH")
    return ""

def parse_latex_pubs(tex_file):
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = {
        "article": r"\\item \{\\bf Journal Articles\}(.*?)\\item \{\\bf Book Chapters\}",
    }

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

                title = re.sub(r'\\href{.*?}{(.*?)}', r'\1', title)
                title = title.replace('\\', '').replace('{', '').replace('}', '')

                get_image_for_pub(title)

parse_latex_pubs('/app/michler_cv.tex')
