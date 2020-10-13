from urllib.parse import urlparse

def parse_url(url:str)->str:
    parse_res = urlparse(url)
    return (parse_res.scheme, parse_res.netloc, parse_res.path)
