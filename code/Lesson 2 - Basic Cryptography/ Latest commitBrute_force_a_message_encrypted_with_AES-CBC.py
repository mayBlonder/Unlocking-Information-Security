from Crypto.Cipher import AES
from Crypto import Random
import itertools
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.prev_func import aes_decrypt, is_english

def aes_decrypt(ciphertext:str, key:str)->str:
    cipher = AES.new(key, AES.MODE_CBC, ciphertext[0:16])
    return cipher.decrypt(ciphertext[16:])

def brute_force_aes(ciphertext:str)->(str, str): 
    key_s = "036"
    key_e = "0000000"
    for num in range(999999):                               #generates all keys
        key = (key_s + str(num).zfill(6) + key_e)
        plaintext = aes_decrypt(ciphertext, key)
        if(is_english(str(plaintext))):
            return plaintext.decode("utf8") , key.encode("utf8")
 
