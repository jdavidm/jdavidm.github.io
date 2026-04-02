import re

with open('/app/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's switch to a sophisticated dark slate/emerald or maroon palette instead of blue/yellow.
# "UofA" colors are cardinal red and navy blue. The user might appreciate cardinal red and a neutral slate.
# Let's use:
# Primary: #CC0033 (UA Red)
# Primary Light: #E53935
# Primary Dark: #990000
# Accent: #002D62 (UA Blue) - used sparingly
# Let's see if the user likes this better. Or maybe a neutral monochromatic scheme with red accents.

replacements = {
    r'--color-primary: #1e3a8a; /\* Deep Navy Blue \*/': '--color-primary: #8B0015; /* Cardinal Red */',
    r'--color-primary-light: #3b82f6;': '--color-primary-light: #C41E3A;',
    r'--color-primary-dark: #1e40af;': '--color-primary-dark: #5C0010;',
    r'--color-accent: #f59e0b; /\* Muted Gold/Amber for interactive elements \*/': '--color-accent: #0C2340; /* Navy Blue Accent */',
    r'--color-accent-hover: #d97706;': '--color-accent-hover: #1D428A;'
}

new_css = css
for pattern, replacement in replacements.items():
    new_css = re.sub(pattern, replacement, new_css)

with open('/app/style.css', 'w', encoding='utf-8') as f:
    f.write(new_css)
