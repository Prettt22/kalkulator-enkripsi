# Muhammad Prasetya Nugroho
# 22552011054
# 222PC

import hashlib
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def hash_function(data):
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    return hashed_data

def main_hash():
    while True:
        clear()
        print("Program Kalkulator Enkripsi Hash SHA256\nBy MPN | 22552011054 | 222PC")
        print("Masukkan angka 0 untuk keluar")

        plaintext = input("\nMasukkan plaintext: ")
        if plaintext == '0':
            clear()
            print("Terima kasih.. Program By MPN | 22552011054 | 222PC")
            break
        else:
            hashed_text = hash_function(plaintext)
            print("Hashed text:", hashed_text)
            input("Tekan Enter untuk reset...")

if __name__ == "__main__":
    main_hash()
