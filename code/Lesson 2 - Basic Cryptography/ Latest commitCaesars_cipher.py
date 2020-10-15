alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext:str, k:str)->str:
    ciphertext = ""    
    for letter in plaintext:
        ciphertext += alphabet[alphabet.index(letter) + k]
    return ciphertext
