from hashlib import sha1 

def sign(line):
    sha = sha1()
    sha.update(line)
    return sha.digest()

def scan(paths, signature):
    suspicius_paths = [] 
    for path in paths:
        with open(path) as file:
            for line in file:
                line = line.rstrip('\n').encode('utf-8')
                if(signature == sign(line)):
                    suspicius_paths.append(path)
                    break
    return suspicius_paths
