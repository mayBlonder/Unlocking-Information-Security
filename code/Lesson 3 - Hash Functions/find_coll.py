from hashlib import md5
from itertools import product
from string import printable

def weak_md5(s):
    return md5(s).digest()[:5]

def find_collisions():
    dic = {}
    for i in range(1,6):
        generator = product(printable, repeat = i)
        for password in generator:
            password = ''.join(password)
            hash1 = weak_md5(password.encode('utf-8'))
            if hash1 not in dic:
                dic[hash1] = password 
            else:
                return (password, dic[hash1])
