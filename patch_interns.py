import re

with open('/app/teaching.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_intern(match):
    name = match.group(1)
    return f'<a href="https://aidelab.arizona.edu/team" target="_blank" style="text-decoration: none;"><span class="badge" style="cursor: pointer;">{name}</span></a>'

new_html = re.sub(r'<span class="badge">(.*?)</span>', replace_intern, html)

with open('/app/teaching.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
