from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Replace with your actual key
key = b'BenjaminFranklin'

ciphertexts = {
    "Push swap": "VABB7yO9xm7xWXROeASsmsgnY0o0sDMJev7zFHhwQS8mvM8V5xQQpLc6cDCFXDWTiFzZ2H9skYkiJ/DpQtnM/uZ0",
    "minitalk": "VAAe8ElCrUAbXivz0ueiIpv/u/ia9PL50+HI+8/bgPKLESHlptPLpu0PW9zWV/LwDVaOqCRCGu6Gopk1X0i6Kn7t",
    "pipex": "VACsSfsWN1cy33ROeASsmsgnY0o0sDMJev7zFHhwQS8mvM8V5xQQpLc6cDCFXDWTiFzZ2H9skYkiJ/DpQtnM/uZ0",
    "so long": "VAA0DAYFf07ym3ROeASsmsgnY0o0sDMJev7zFHhwQS8mvM8V5xQQpLc6cDCFXDWTiFzZ2H9skYkiJ/DpQtnM/uZ0",
    "fdf": "VADYjxBiOQSAWNqB652klCj13URaziELdHd+2Z38XCMD9dvO9tSyFob6Il3NBX9YXrgZEiQK7JZJ7w5t0N80wMl7",
    "fractol": "VAD2sO2qgbqPEXROeASsmsgnY0o0sDMJev7zFHhwQS8mvM8V5xQQpLc6cDCFXDWTiFzZ2H9skYkiJ/DpQtnM/uZ0"
}

def decrypt_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decoded_data = base64.b64decode(ciphertext)
    decrypted_data = cipher.decrypt(decoded_data)
    try:
        return unpad(decrypted_data, AES.block_size).decode('utf-8')
    except ValueError as e:
        print(f"Padding error: {e}")
        return decrypted_data.decode('utf-8')

for name, ciphertext in ciphertexts.items():
    try:
        decrypted_message = decrypt_ecb(ciphertext, key)
        print(f"{name}: {decrypted_message}")
    except Exception as e:
        print(f"Failed to decrypt {name}: {e}")