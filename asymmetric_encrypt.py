# Muhammad Prasetya Nugroho
# 22552011054
# 222PC
# butuh modul PyCryptoDome "pip install pycryptodome"

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def asymmetric_encrypt(plaintext, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext

def asymmetric_decrypt(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(ciphertext).decode()
    return plaintext

def main_asymmetric():
    clear()
    print("Program Enkripsi Asymmetric\nBy MPN | 22552011054 | 222PC")
    key_pair = RSA.generate(2048)
    private_key = key_pair.export_key()
    public_key = key_pair.publickey()

    plaintext = input("\nMasukkan plaintext: ")
    ciphertext = asymmetric_encrypt(plaintext, public_key)
    print("Cipher text:", ciphertext.hex())

    decrypted_text = asymmetric_decrypt(ciphertext, RSA.import_key(private_key))
    print("Plaintext setelah didekripsi:", decrypted_text)

if __name__ == "__main__":
    main_asymmetric()
