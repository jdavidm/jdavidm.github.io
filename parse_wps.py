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
                items.append(line.replace('\\subitem', '').strip())
            elif items and line and not line.startswith('\\') and not line.startswith('202'):
                items[-1] += ' ' + line.strip()

        return items
    except ValueError:
        return []

def clean_item(item):
    text = item.replace(r'\textbf', '').replace('{', '').replace('}', '').replace(r'\$', '')
    text = re.sub(r'\\href{([^}]+)}\{([^}]+)\}', r'<a href="\1">\2</a>', text)
    text = re.sub(r'\\url{([^}]+)}', r'<a href="\1">\1</a>', text)
    text = text.replace(r'\emph', '')
    text = text.replace(r"\'e", 'é').replace(r"\'o", 'ó').replace(r'\"o', 'ö')
    return text.strip()

print("--- BOOK CHAPTERS ---")
book_chapters = get_items(r'\item {\bf Book Chapters}', r'\item {\bf In Review}')
for bc in book_chapters:
    if bc:
        print(clean_item(bc))

print("\n--- IN REVIEW ---")
in_review = get_items(r'\item {\bf In Review}', r'\item {\bf In Preparation}')
for ir in in_review:
    if ir:
        print(clean_item(ir))

print("\n--- IN PREPARATION ---")
in_prep = get_items(r'\item {\bf In Preparation}', r'\item {\bf Reports, Briefs, and Policy Papers}')
for ip in in_prep:
    if ip:
        print(clean_item(ip))

print("\n--- REPORTS ---")
reports = get_items(r'\item {\bf Reports, Briefs, and Policy Papers}', r'\item {\bf Invited Seminars, Conference Presentations, and Workshops}')
for r in reports:
    if r:
        print(clean_item(r))
