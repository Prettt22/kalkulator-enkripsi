# Muhammad Prasetya Nugroho
# 22552011054
# 222PC
# butuh modul PyCryptoDome "pip install pycryptodome"

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def symmetric_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
    return ciphertext, cipher.nonce, tag

def symmetric_decrypt(ciphertext, key, nonce, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag).decode()
    return plaintext

def main_symmetric():
    clear()
    print("Program Enkripsi Asymmetric\nBy MPN | 22552011054 | 222PC")
    key = get_random_bytes(16)  # 16 bytes = 128-bit key
    print("\nKunci enkripsi:", key.hex())

    plaintext = input("Masukkan plaintext: ")
    ciphertext, nonce, tag = symmetric_encrypt(plaintext, key)
    print("Cipher text:", ciphertext.hex())

    decrypted_text = symmetric_decrypt(ciphertext, key, nonce, tag)
    print("Plaintext setelah didekripsi:", decrypted_text)

if __name__ == "__main__":
    main_symmetric()
