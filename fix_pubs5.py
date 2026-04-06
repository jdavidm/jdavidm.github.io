import re

with open('publications.html', 'r') as f:
    html = f.read()

# I see the problem. The user wants the working papers and book chapters formatted *exactly* like publications.
# This means NO background images on the cards. They should just have a white background with a colored tag, title, authors, journal.

# Let's completely replace the injected sections again.
html = re.sub(r'<!-- Book Chapters Section -->.*?</main>', '</main>', html, flags=re.DOTALL)

with open('publications.html', 'w') as f:
    f.write(html)
