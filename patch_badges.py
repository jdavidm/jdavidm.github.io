import re

with open('index.html', 'r') as f:
    content = f.read()

replacements = [
    (re.compile(r'<span class="badge">Associate Editor, American Journal of Agricultural Economics \(2026-\)</span>'),
     r'<a href="https://onlinelibrary.wiley.com/journal/14678276" target="_blank" rel="noopener noreferrer">Associate Editor, American Journal of Agricultural Economics (2026-)</a>'),
    (re.compile(r'<span class="badge">Associate Editor, European Review of Agricultural Economics \(2024-\)</span>'),
     r'<a href="https://academic.oup.com/erae" target="_blank" rel="noopener noreferrer">Associate Editor, European Review of Agricultural Economics (2024-)</a>'),
    (re.compile(r'<span class="badge">Associate Editor, Agricultural Economics \(2023-\)</span>'),
     r'<a href="https://onlinelibrary.wiley.com/journal/15740862" target="_blank" rel="noopener noreferrer">Associate Editor, Agricultural Economics (2023-)</a>')
]

for pattern, new in replacements:
    content = pattern.sub(new, content)

with open('index.html', 'w') as f:
    f.write(content)

print("Badges patched successfully!")
