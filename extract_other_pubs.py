import re

def parse_tex_section(content, section_name):
    # Find the section and extract items until the next section
    section_pattern = re.compile(rf'\\section{{\s*{section_name}\s*}}([\s\S]*?)(?:\\section{{|$)', re.IGNORECASE)
    match = section_pattern.search(content)
    if not match:
        return []

    section_content = match.group(1)

    # Extract \item entries
    items = []
    current_item = ""
    for line in section_content.split('\n'):
        line = line.strip()
        if line.startswith(r'\item'):
            if current_item:
                items.append(current_item.strip())
            current_item = line[5:].strip()
        elif current_item and not line.startswith(r'\begin') and not line.startswith(r'\end'):
            current_item += " " + line
    if current_item:
        items.append(current_item.strip())

    return items

def extract_metadata(item_text):
    # Very basic extraction - LaTeX parsing is complex, so we'll do our best
    # Usually format is: Authors. Year. "Title." \emph{Journal} ...

    # Clean up common LaTeX
    text = item_text.replace(r'\textbf', '').replace('{', '').replace('}', '').replace(r'\$', '')
    text = re.sub(r'\\href{([^}]+)}\{([^}]+)\}', r'<a href="\1">\2</a>', text)
    text = re.sub(r'\\url{([^}]+)}', r'<a href="\1">\1</a>', text)
    text = text.replace(r'\emph', '')
    text = text.replace(r"\'e", 'é').replace(r"\'o", 'ó')

    return text

with open('michler_cv.tex', 'r') as f:
    content = f.read()

print("--- WORKING PAPERS ---")
wps = parse_tex_section(content, "Working Papers")
for wp in wps:
    print(extract_metadata(wp))
    print("-" * 40)

print("\n--- BOOK CHAPTERS ---")
bcs = parse_tex_section(content, "Book Chapters")
for bc in bcs:
    print(extract_metadata(bc))
    print("-" * 40)
