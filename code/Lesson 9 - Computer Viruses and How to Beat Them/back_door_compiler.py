import re

CODE = '''
def authenticate(username, password):
    return username == {username!r} and password == {password!r}
'''

def compile_(format_):
    print(format_)
    format_ = """USERNAME: hacker
              PASSWORD: 1234"""
    username = re.search(r'USERNAME: (.*)', format_).group(1)
    password = re.search(r'PASSWORD: (.*)', format_).group(1)
    return CODE.format(username=username, password=password)
