with open('publications.html', 'r', encoding='utf-8') as f:
    html = f.read()
import re
html = re.sub(r'<h3 class="pub-title">\s*hrefhttps://doi.org/10.1002/aepp.13133Ulysses\s*</h3>', '<h3 class="pub-title">Ulysses\' Pact or Ulysses\' Raft: Using Pre-Analysis Plans in Experimental and Nonexperimental Research</h3>', html)
with open('publications.html', 'w', encoding='utf-8') as f:
    f.write(html)
