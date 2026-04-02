import re

with open('/app/publications.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('pubs_html.txt', 'r', encoding='utf-8') as f:
    pubs_html = f.read()

# Replace everything inside <div class="pub-grid" id="pub-grid"> ... </div>
pattern = r'(<div class="pub-grid[^>]*id="pub-grid"[^>]*>).*?(</div>\s*<div style="text-align: center; margin-top: 3rem;">)'
new_html = re.sub(pattern, r'\1\n' + pubs_html + r'\2', html, flags=re.DOTALL)

with open('/app/publications.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
