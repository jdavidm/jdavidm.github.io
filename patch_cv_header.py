import re

with open('cv.html', 'r') as f:
    content = f.read()

header_replacement = """    <!-- Hero Section -->
    <header class="hero page-header" style="min-height: 40vh; text-align: center; padding: 0;">
        <img src="https://source.unsplash.com/random/1600x900/?office,desk,books" alt="CV Background" class="hero-bg" onerror="this.src='https://images.unsplash.com/photo-1456324504439-367cee3b3c32?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80'">
        <div class="container relative z-10" style="padding-top: var(--spacing-xl); padding-bottom: var(--spacing-lg);">
            <div class="hero-content">
                <h1 class="animate-on-scroll" style="color: white; margin-bottom: 1rem;">Curriculum Vitae</h1>
                <p class="animate-on-scroll" style="max-width: 600px; margin: 0 auto; color: #e2e8f0; font-size: 1.25rem;">Complete details of my academic background, appointments, and research.</p>
            </div>
        </div>
    </header>"""

old_header = r'    <!-- Page Header -->\n    <header class="page-header">\n        <div class="container">\n            <h1 class="animate-on-scroll">Curriculum Vitae</h1>\n            <p class="animate-on-scroll">Complete details of my academic background, appointments, and research.</p>\n        </div>\n    </header>'

content = re.sub(old_header, header_replacement, content)

with open('cv.html', 'w') as f:
    f.write(content)
print("Updated cv.html header")
