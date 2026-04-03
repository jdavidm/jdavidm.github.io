import re

with open('publications.html', 'r') as f:
    html = f.read()

# The issue is that the old script generated HTML with class="publication-grid" and class="publication-card",
# but the rest of the site uses "pub-grid" and "pub-card" for publications (based on the previous PRs).
# The Working Papers and Book Chapters were injected after a </div> and </main>.

# Let's remove the previously injected HTML (everything from "<!-- Working Papers Section -->" onwards, up to </main>)
html = re.sub(r'<!-- Working Papers Section -->.*?</main>', '</main>', html, flags=re.DOTALL)
html = re.sub(r'<!-- Book Chapters Section -->.*?</main>', '</main>', html, flags=re.DOTALL)

with open('publications.html', 'w') as f:
    f.write(html)
