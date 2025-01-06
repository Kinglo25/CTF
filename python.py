import base64

# Replace with your actual keys
keys = []
# Write all possible variations of the keys to a file
with open("words.txt", "w") as f:
    for key in keys:
        f.write(key + "\n")
        f.write(key.replace('-', '1').replace('.', '0') + "\n")
        f.write(key.lower() + "\n")
        f.write(key.title() + "\n")
        f.write(key.upper() + "\n")
        f.write(key.replace(' ', '') + "\n")
        f.write(key.replace(' ', '').lower() + "\n")
        f.write(key.title().replace(' ', '') + "\n")
        f.write(key.replace(' ', '').title() + "\n")
        f.write(key.replace(' ', '').upper() + "\n")
        f.write(key.replace(' ', '').lower().title() + "\n")
        f.write(key[0].upper() + key[1:] + "\n")
        f.write(key.replace(' ', '-') + "\n")
        f.write(key.replace(' ', '-').lower() + "\n")
        f.write(key.replace(' ', '-').upper() + "\n")

