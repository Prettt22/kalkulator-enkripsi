# Muhammad Prasetya Nugroho
# 22552011054
# 222PC

import os
def caesar_cipher_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Hanya enkripsi karakter alfabet
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            ciphertext += chr(shifted)
        else:
            ciphertext += char  # Biarkan karakter non-alfabet tidak terenkripsi
    return ciphertext

def caesar_cipher_decrypt(ciphertext, key):
    return caesar_cipher_encrypt(ciphertext, -key)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear()
        print("Program Kalkulator Enkripsi Caesar\nBy MPN | 22552011054 | 222PC")
        print("\nMenu:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("0. Keluar")

        choice = input("Silahkan masukkan nomor menu: ")
        if choice == '1':
            clear()
            plaintext = input("Masukkan plaintext: ")
            key = int(input("Masukkan nilai kunci enkripsi: "))
            ciphertext = caesar_cipher_encrypt(plaintext, key)
            print("Cipher text:", ciphertext)
            input("Tekan Enter untuk kembali ke menu...")
        elif choice == '2':
            clear()
            ciphertext = input("Masukkan ciphertext: ")
            key = int(input("Masukkan nilai kunci dekripsi: "))
            plaintext = caesar_cipher_decrypt(ciphertext, key)
            print("Plain text:", plaintext)
            input("Tekan Enter untuk kembali ke menu...")
        elif choice == '0':
            clear()
            print("Terima kasih.. Program By MPN | 22552011054 | 222PC")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan '1', '2', atau '0'.")
            input("Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
