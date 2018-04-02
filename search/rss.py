import requests
def search(name):
    r = requests.get(url, allow_redirects = False)
    if r.status_code == 200:
        return name
    else:
        return ''

