import re

def get_items(start_marker, end_marker=None):
    with open('michler_cv.tex', 'r') as f:
        content = f.read()

    try:
        start_idx = content.index(start_marker)
        if end_marker:
            try:
                end_idx = content.index(end_marker, start_idx)
                section_content = content[start_idx:end_idx]
            except ValueError:
                section_content = content[start_idx:]
        else:
            section_content = content[start_idx:]

        items = []
        for line in section_content.split('\n'):
            line = line.strip()
            if line.startswith('\\subitem'):
                # remove any [number] part if present (e.g. \subitem[16])
                line = re.sub(r'\\subitem(?:\[\d+\])?', '', line).strip()
                items.append(line)
            elif items and line and not line.startswith('\\') and not line.startswith('202'):
                items[-1] += ' ' + line.strip()

        return items
    except ValueError:
        return []

def clean_item(item):
    # First extract hrefs properly before removing brackets
    def href_replacer(match):
        url = match.group(1)
        text = match.group(2)
        return f'<a href="{url}" target="_blank">{text}</a>'

    text = re.sub(r'\\href{([^}]+)}{([^}]+)}', href_replacer, item)

    text = text.replace(r'\textbf', '').replace('{', '').replace('}', '').replace(r'\$', '')
    text = text.replace(r'\emph', '')
    text = text.replace(r"\'e", 'é').replace(r"\'o", 'ó').replace(r'\"o', 'ö')
    text = text.replace('``', '"').replace("''", '"')
    text = text.replace('\\\\', '').strip()
    return text

print("--- BOOK CHAPTERS ---")
book_chapters = get_items(r'\item {\bf Book Chapters}', r'\item {\bf In Review}')
for bc in book_chapters:
    if bc:
        print(clean_item(bc))

print("\n--- IN REVIEW / IN PREPARATION ---")
in_review = get_items(r'\item {\bf In Review}', r'\item {\bf In Preparation}')
in_prep = get_items(r'\item {\bf In Preparation}', r'\item {\bf Reports, Briefs, and Policy Papers}')
for ir in in_review + in_prep:
    if ir:
        print(clean_item(ir))
