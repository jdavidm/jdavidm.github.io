import re

with open('/app/teaching.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_student_card(match):
    name = match.group(1)
    details = match.group(2)
    # create slug for url
    slug = name.lower().replace(' ', '-')
    return f'''<a href="https://aidelab.arizona.edu/team" target="_blank" style="text-decoration: none; color: inherit;">
                            <li class="student-card">
                                <div class="student-name">{name} <i class="fas fa-external-link-alt" style="font-size: 0.8em; color: var(--color-primary-light); margin-left: 4px;"></i></div>
                                <div class="student-details">{details}</div>
                            </li>
                        </a>'''

new_html = re.sub(r'<li class="student-card">\s*<div class="student-name">(.*?)</div>\s*<div class="student-details">(.*?)</div>\s*</li>', replace_student_card, html)

with open('/app/teaching.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
