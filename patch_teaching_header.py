import re

with open('teaching.html', 'r') as f:
    content = f.read()

header_replacement = """    <!-- Hero Section -->
    <header class="hero page-header" style="min-height: 40vh; text-align: center; padding: 0;">
        <img src="https://source.unsplash.com/random/1600x900/?university,classroom" alt="Teaching Background" class="hero-bg" onerror="this.src='https://images.unsplash.com/photo-1524178232363-1fb2b075b655?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80'">
        <div class="container relative z-10" style="padding-top: var(--spacing-xl); padding-bottom: var(--spacing-lg);">
            <div class="hero-content">
                <h1 class="animate-on-scroll" style="color: white; margin-bottom: 1rem;">Teaching & Mentorship</h1>
                <p class="animate-on-scroll" style="max-width: 600px; margin: 0 auto; color: #e2e8f0; font-size: 1.25rem;">Details of the university courses I teach and the undergraduate and graduate students I advise.</p>
            </div>
        </div>
    </header>"""

old_header = r'    <!-- Page Header -->\n    <header class="page-header" style="background-color: var\(--color-primary-dark\); color: white; padding: var\(--spacing-xl\) 0 var\(--spacing-lg\) 0; text-align: center;">\n        <div class="container">\n            <h1 class="animate-on-scroll">Teaching & Mentorship</h1>\n            <p class="animate-on-scroll" style="max-width: 600px; margin: 0 auto; color: #e2e8f0;">Details of the university courses I teach and the undergraduate and graduate students I advise.</p>\n        </div>\n    </header>'

content = re.sub(old_header, header_replacement, content)

with open('teaching.html', 'w') as f:
    f.write(content)
print("Updated teaching.html header")
