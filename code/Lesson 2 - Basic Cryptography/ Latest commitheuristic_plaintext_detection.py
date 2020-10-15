from collections import Counter

def is_ascii(s:str)->bool:
    return all(ord(c) < 128 for c in s)

def is_english(s:str)->bool:
    if(is_ascii(s) == False):
        return False
  
    cnt = Counter()
    for letter in s:
        cnt[letter] += 1
    cnt[' '] = 0
        
    for letter in cnt.most_common(3):
        if(letter[0] not in ('e', 't', 'a', 'o', 'i', 'n')):
            return False
    return True
