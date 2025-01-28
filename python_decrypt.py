import subprocess
from itertools import permutations, product
from collections import defaultdict

def generate_passwords(word_list, combination_length):
    length_map = defaultdict(list)
    for word in word_list:
        length_map[len(word)].append(word)

    target_length = 10
    valid_combinations = []

    def find_combinations(current, remaining, depth):
        if depth == 1:
            if remaining in length_map:
                valid_combinations.append(current + [remaining])
            return
            
        start = current[-1] if current else 1
        max_part = remaining // depth
        for l in range(start, max_part + 1):
            new_remaining = remaining - l
            if new_remaining >= l * (depth - 1):
                find_combinations(current + [l], new_remaining, depth - 1)

    find_combinations([], target_length, combination_length)

    for lengths in valid_combinations:
        pools = [length_map[length] for length in lengths]
        for words in product(*pools):
            for perm in permutations(words):
                yield ''.join(perm)

def process_chunk(chunk, variation_file, usernames):
    buffer = []
    for i in range(1, 4):
        gen = generate_passwords(chunk, i)
        for password in gen:
            buffer.extend(f"{user}  {password}\n" for user in usernames)
    
    variation_file.writelines(buffer)
    variation_file.flush()
    
    print("Running John the Ripper...")
    subprocess.run([
        "./john/run/john",
        "--wordlist=variation.txt",
        "--pot=cracked.txt",
        "--format=NT",
        "--fork=6",
        "hashes.txt"
    ], check=True)
    variation_file.seek(0)
    variation_file.truncate()

if __name__ == "__main__":
    base_usernames = {
        'GrandmaCOBOL', 'AmazingGrace', 'Grace.Hopper',
        'Grace_Hopper', 'Ada_Lovelace', 'Ada.Lovelace',
        'Ada Lovelace', 'Grace Hopper', 'AdaLovelace:',
        'GraceHopper:'
    }
    
    usernames = set()
    for user in base_usernames:
        usernames.update({user, user.lower(), user.upper()})

    CHUNK_SIZE = 1000
    with open('wordlist.txt', 'r') as f, open('variation.txt', 'w+') as variation:
        chunk = set()
        for line in f:
            chunk.update(word.strip() for word in line.split())
            if len(chunk) >= CHUNK_SIZE:
                process_chunk(chunk, variation, usernames)
                chunk.clear()
        
        if chunk:
            process_chunk(chunk, variation, usernames)