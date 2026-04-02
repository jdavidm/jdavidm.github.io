import re

with open('/app/teaching.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix student cards
def replace_student_link(match):
    name = match.group(1)
    # Extract just the name part before the icon
    clean_name = re.sub(r'\s*<i.*?></i>', '', name).strip()
    slug = clean_name.lower().replace(' ', '-')
    details = match.group(2)
    return f'''<a href="https://aidelab.arizona.edu/person/{slug}" target="_blank" style="text-decoration: none; color: inherit;">
                            <li class="student-card">
                                <div class="student-name">{name}</div>
                                <div class="student-details">{details}</div>
                            </li>
                        </a>'''

# Original HTML was replaced with the team URL in the previous step
pattern_card = r'<a href="https://aidelab\.arizona\.edu/team" target="_blank"[^>]*>\s*<li class="student-card">\s*<div class="student-name">(.*?)</div>\s*<div class="student-details">(.*?)</div>\s*</li>\s*</a>'
new_html = re.sub(pattern_card, replace_student_link, html)

# Fix Intern Badges
def replace_intern_link(match):
    name = match.group(1)
    slug = name.lower().replace(' ', '-')
    return f'<a href="https://aidelab.arizona.edu/person/{slug}" target="_blank" style="text-decoration: none;"><span class="badge" style="cursor: pointer;">{name}</span></a>'

pattern_badge = r'<a href="https://aidelab\.arizona\.edu/team" target="_blank"[^>]*><span class="badge"[^>]*>(.*?)</span></a>'
new_html = re.sub(pattern_badge, replace_intern_link, new_html)


with open('/app/teaching.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
