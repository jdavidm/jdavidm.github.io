import re

with open('publications.html', 'r') as f:
    html = f.read()

# I see the problem. The main publications grid uses a different layout. Wait, let me check the CSS for .pub-card and .pub-grid
# Actually, the user asked to format them "just like you did publications".
# The main publications grid has cards that look like this:
# <div class="pub-card" data-category="journal" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('...');">
#  <span class="card-tag">Journal</span>
#  <h3 class="pub-title">...</h3>
#  <p class="pub-authors">...</p>
#  <p class="pub-journal">...</p>
#  <div class="pub-links">...</div>
# </div>

# Oh wait! In my fix_pubs2.py, I wrapped the interior of my injected pub-cards with `<div class="card-overlay" style="...">`.
# The main publications DO NOT use `.card-overlay` inside `.pub-card`! The `.pub-card` itself is a flex container.

# Let's clean up the injected working papers and book chapters to remove card-overlay.
html = html.replace('<div class="card-overlay" style="padding: 1.5rem; position: relative; z-index: 2;">', '')
html = html.replace('</div>\n        </div>\n\n        <div class="pub-card"', '        </div>\n\n        <div class="pub-card"')
html = html.replace('</div>\n        </div>\n    </div>', '        </div>\n    </div>')

with open('publications.html', 'w') as f:
    f.write(html)
