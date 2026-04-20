import re

files_to_update = {
    'index.html': 'photos/IMG_8410-2.jpg',
    'publications.html': 'photos/IMG_7551.jpg',
    'teaching.html': 'photos/IMG_9513.jpg',
    'cv.html': 'photos/DSC_0216.jpg',
    'software.html': 'photos/IMG_2588.JPG'
}

# Pattern to match the img tag that has class="hero-bg"
pattern = re.compile(r'<img[^>]+class="hero-bg"[^>]*>|<img[^>]*class="hero-bg"[^>]+>', re.IGNORECASE)
src_pattern = re.compile(r'src="[^"]+"')

for filepath, image_src in files_to_update.items():
    try:
        with open(filepath, 'r') as f:
            content = f.read()

        def repl(match):
            m = match.group(0)
            return src_pattern.sub(f'src="{image_src}"', m)

        new_content = pattern.sub(repl, content)

        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    except FileNotFoundError:
        print(f"Skipping {filepath} - not found")
