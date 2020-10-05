alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext:str, k:str)->str:
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)

def decrypt(ciphertext:str, k:str)->str:
    return encrypt(ciphertext, -k)
    
def brute_force(ciphertext:str):
    for i in range(26):
        print(decrypt(ciphertext, i))
    
brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")
