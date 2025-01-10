from base64 import b64encode

def main():
    flag = ''
    with open('fdf.bfe', 'rb') as f:
        flag = f.read()
    print(b64encode(flag).decode())
    with open('new_text.txt.bfe', 'wb') as f:
        f.write(flag)

if __name__ == '__main__':
    main()
