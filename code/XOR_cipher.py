def encrypt(plaintext:str, k:str)->str:
    cipertext = ""
    for i, letter in enumerate(plaintext):
        cipertext += chr(ord(plaintext[i]) ^ ord(k[i]))
    return cipertext
