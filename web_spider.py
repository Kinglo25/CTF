import requests
from bs4 import BeautifulSoup
import re
import subprocess

def extract_text_and_numbers(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return '', [], []

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all text
    text = soup.get_text()

    # Remove punctuation from the text
    text = re.sub(r'[^\w\s]', '', text)

    # Extract all numbers using regular expressions
    numbers = re.findall(r'\d+', text)

    # Extract all URLs and their text
    url_texts = [a.get_text() for a in soup.find_all('a', href=True)]
    url_texts = [re.sub(r'[^\w\s]', '', text) for text in url_texts]

    return text, numbers, url_texts

def crawl(url, depth):
    if depth == 0:
        return

    print(f"Crawling: {url}")
    text, numbers, url_texts = extract_text_and_numbers(url)
    with open('wordlist.txt', 'w') as f:
        for word in text.split():
            f.write(word.capitalize() + '\n')
            f.write(word.lower() + '\n')
            f.write(word.upper() + '\n')
        for number in numbers:
            f.write(number + '\n')
        for word in url_texts:
            f.write(word.capitalize() + '\n')
            f.write(word.lower() + '\n')
            f.write(word.upper() + '\n')

    # Call python_decrypt.py to generate passwords
    print("Generating passwords...")
    subprocess.run(['python3', 'python_decrypt.py'])
    print("Passwords generated.")
    # Find all links on the page
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]

    # Crawl each link (with reduced depth)
    for link in links:
        if link.startswith('http'):
            crawl(link, depth - 1)

if __name__ == "__main__":
    open('wordlist.txt', 'w').close()
    start_url = 'https://en.wikipedia.org/wiki/Ada_Lovelace_(microarchitecture)'  # Replace with the starting URL
    crawl(start_url, depth=2)  # Adjust the depth as needed