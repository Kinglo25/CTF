import itertools

# List of keys
keys = ["Nikola", "Tesla", "Current", "Electricity", "AC", "1943", "1856"]

# Function to generate variations
def generate_variations(words):
    variations = set()
    
    # Add original keys
    variations.update(words)
    
    # Add lowercase and uppercase variations
    for word in words:
        variations.add(word.lower())
        variations.add(word.upper())
        variations.add(word.capitalize())

    # Add combinations of keys
    for combo in itertools.permutations(words, 2):
        variations.add(''.join(combo))
        variations.add('_'.join(combo))
        variations.add('-'.join(combo))
        variations.add(''.join(combo).lower())
        variations.add(''.join(combo).upper())

    # # Add numbers to the end of each variation
    # for variation in list(variations):
    #     for i in range(100):  # Add numbers from 0 to 99
    #         variations.add(f"{variation}{i}")
    #         variations.add(f"{i}{variation}")

    return variations

# Generate the dictionary
password_dict = generate_variations(keys)

# Write to a file
with open("password_dictionary.txt", "w") as file:
    for password in password_dict:
        file.write(f"{password}\n")

import base64


# Dictionary mapping characters to Morse code
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', 
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', 
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.',
    ')': '-.--.-', ' ': '/'
}

def text_to_morse(text):
    # Convert text to uppercase and then map each character to its Morse code equivalent
    text = text.upper().replace(' ', '')  # Morse code is case-insensitive
    morse_code = []

    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            # If character is not found in the dictionary, ignore it
            # or add a placeholder (e.g., '?') if you'd prefer to handle unknown chars
            morse_code.append('?')

    return ' '.join(morse_code)


# Write all possible variations of the keys to a file
with open("password_dictionary.txt", "a") as f:
    for key in keys:
        f.write(key + "\n")
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
        f.write(' '.join(format(ord(c), '08b') for c in key) + '\n')
        f.write(text_to_morse(key) + '\n')
        f.write(text_to_morse(key).replace('-', '1').replace('.', '0') + "\n")
        f.write(base64.b64encode(key.encode()).decode() + "\n")



print("Password dictionary generated and saved to password_dictionary.txt")
