import requests
import json

def get()->int:
    r = requests.get("http://httpbin.org/status/204")
    return r.status_code 

def post():
    payload_tuples = [('x', '1'), ('y', '2')]
    r = requests.post("http://httpbin.org/post", data=payload_tuples)
    return r
