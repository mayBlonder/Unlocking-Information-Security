from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def sign(m, private_key):
    return key.sign(m, private_key)

def verify(m, s, public_key):
    return key.verify(m, s)
