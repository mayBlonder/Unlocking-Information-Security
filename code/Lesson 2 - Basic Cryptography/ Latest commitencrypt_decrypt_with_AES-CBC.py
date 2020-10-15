from Crypto.Cipher import AES
from Crypto import Random

def aes_encrypt(plaintext:str, key:str)->str:               
    iv = Random.get_random_bytes(16)			# Random iv.
    cipher = AES.new(key, AES.MODE_CBC, iv)  
    return iv + cipher.encrypt(plaintext)

def aes_decrypt(ciphertext:str, key:str)->str:
    cipher = AES.new(key, AES.MODE_CBC, ciphertext[0:16])
    return cipher.decrypt(ciphertext[16:]).decode()
