from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def encrypt(m, public_key):
    cipher = RSA.importKey(public_key)
    return cipher.encrypt(str(m).encode("utf8"),0)

def decrypt(c, private_key):
    plaintext = RSA.importKey(private_key)
    return plaintext.decrypt(c)
