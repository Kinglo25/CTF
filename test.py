from base64 import b64encode

def main():
    with open('text.txt.bfe', 'rb') as f:
        flag = f.read()
    print(b64encode(flag).decode())
    with open('new_text.txt.bfe', 'rb') as f:
        flag = f.read()
    print(b64encode(flag).decode())

if __name__ == '__main__':
    main()