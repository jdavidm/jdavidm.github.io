import re
import glob

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace target="_blank" with target="_blank" rel="noopener noreferrer"
    # First, let's remove existing rel="noopener noreferrer" or rel="noopener" to avoid duplicates
    content = re.sub(r'target="_blank"\s+rel="noopener noreferrer"', 'target="_blank"', content)
    content = re.sub(r'target="_blank"\s+rel="noopener"', 'target="_blank"', content)

    # Also handle if rel comes before target?
    # Better approach: find all <a ...> tags and modify them.

    def process_match(match):
        tag = match.group(0)
        if 'target="_blank"' in tag:
            # Remove any existing rel attribute to simplify (assuming no other rel is needed like 'nofollow')
            # Let's just remove rel="noopener noreferrer" specifically
            tag = tag.replace('rel="noopener noreferrer"', '')
            tag = tag.replace('rel="noopener"', '')
            # Now add it after target="_blank"
            tag = tag.replace('target="_blank"', 'target="_blank" rel="noopener noreferrer"')
            # clean up multiple spaces
            tag = re.sub(r'\s+', ' ', tag)
            tag = tag.replace(' >', '>')
            # restore newlines if we messed them up? The regex r'<a[^>]+>' might match across newlines
            # If we just replace inside the tag, it's fine.
        return tag

    # regex to match <a ...>
    content = re.sub(r'<a\s+[^>]+>', process_match, content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
