from hashlib import sha1
import sys

ipad = b'123455678'
opad = b'abcdefghi'

def weak_hmac(m, k, ipad, opad):
    str_m = str(int.from_bytes(m, sys.byteorder))
    int_k = int.from_bytes(k, sys.byteorder)
    int_ipad = int.from_bytes(ipad, sys.byteorder)
    int_opad = int.from_bytes(opad, sys.byteorder)
    
    k_xor_ipad = str(int_k ^ int_ipad)
    k_xor_opad = str(int_k ^ int_opad)
    
    sha_part1 = (k_xor_ipad + str_m).encode()
    sha_part1 = sha1(sha_part1).hexdigest()
    return sha1((k_xor_opad + str(sha_part1)).encode()).hexdigest()
