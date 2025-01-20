import itertools
from passlib.hash import nthash

def generate_passwords(word_list, longueur_combinaison):
    for combinaison in itertools.permutations(word_list, longueur_combinaison):
        password = ''.join(combinaison)
        if len(password) == 10:
            yield password

def process_chunk(chunk, variation_file):
    for i in range(1, 2):
        for password in generate_passwords(chunk, i):
            variation_file.write('GrandmaCOBOL  ' + password + '\n')
            variation_file.write('GrandmaCOBOL\t' + password + '\n')
            variation_file.write('AmazingGrace  ' + password + '\n')
            variation_file.write('AmazingGrace\t' + password + '\n')
            variation_file.write('Grace Hopper  ' + password + '\n')
            variation_file.write('Grace Hopper\t' + password + '\n')
            variation_file.write('Grace.Hopper  ' + password + '\n')
            variation_file.write('Grace.Hopper\t' + password + '\n')
            variation_file.write('Grace_Hopper  ' + password + '\n')
            variation_file.write('Grace_Hopper\t' + password + '\n')
            

if __name__ == "__main__":
    chunk_size = 100000  # Adjust the chunk size as needed

    with open('words.txt', 'r') as fichier, open('variation.txt', 'w') as variation:
        chunk = []
        for ligne in fichier:
            chunk.append(ligne.strip())
            if len(chunk) >= chunk_size:
                process_chunk(chunk, variation)
                chunk = []
        
        # Process any remaining lines in the last chunk
        if chunk:
            process_chunk(chunk, variation)
