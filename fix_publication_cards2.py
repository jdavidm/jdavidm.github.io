import re

with open('publications.html', 'r') as f:
    html = f.read()

# I want to find the exact cards from aidelab. Let's see if we can just wrap the ones we can determine the exact URL for
