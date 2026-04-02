import re

with open('publications.html', 'r') as f:
    content = f.read()

# Change the alpha values from 0.7/0.9 to 0.4/0.7 to make the background more visible
content = re.sub(r'rgba\(15, 23, 42, 0\.7\)', 'rgba(15, 23, 42, 0.4)', content)
content = re.sub(r'rgba\(15, 23, 42, 0\.9\)', 'rgba(15, 23, 42, 0.7)', content)

with open('publications.html', 'w') as f:
    f.write(content)

print("Updated publication background opacities")
