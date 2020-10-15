
def simple_hash(s):
    r = 7
    for letter in s:
        r = (r * 31 + ord(letter)) % 2**16
    return r
