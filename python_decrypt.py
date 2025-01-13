import itertools
from passlib.hash import nthash

def generate_passwords(word_list, longueur_combinaison=1):
    return [''.join(combinaison) for combinaison in itertools.permutations(word_list, longueur_combinaison)]

if __name__ == "__main__":
    # Charger les words depuis un fichier
    with open('words.txt', 'r') as fichier:
        words = [ligne.strip() for ligne in fichier]
    passwords = []
    # Générer les words de passe
    for i in range(1, 4):
        passwords.extend(generate_passwords(words, i))
    variation = []
    for password in passwords:
        variation.append(password)
        variation.append(password.lower())
        variation.append(password.upper())
        variation.append(password.capitalize())
        variation.append(password.replace(' ', ''))
    
    # Enregistrer les words de passe dans un fichier
    with open('variation.txt', 'w') as fichier:
        for password in variation:
            fichier.write(password + '\n')
    for password in variation:
        h = "796ba5a53df1352e06cc7b0f3ad2a41d"
        if nthash.verify(password, h):
            print(f"Password found: {password}")
            break
