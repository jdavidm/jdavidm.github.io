import re

with open('/app/publications.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change the linear-gradient rgba values to be less dark
html = re.sub(r'rgba\(15, 23, 42, 0\.7\)', r'rgba(15, 23, 42, 0.4)', html)
html = re.sub(r'rgba\(15, 23, 42, 0\.9\)', r'rgba(15, 23, 42, 0.7)', html)

with open('/app/publications.html', 'w', encoding='utf-8') as f:
    f.write(html)
