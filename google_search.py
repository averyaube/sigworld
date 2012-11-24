import requests
from urllib import urlencode

SEARCH_URL = "https://www.googleapis.com/customsearch/v1"
SEARCH_KEY = "AIzaSyBfcML2T3Jk7kgRxGpucr3vt1OsVMQ7VMI"
SEARCH_CX = "013787973175003050528:h9hmq1k801a"


def image_search(term):
    return search_call({
        'q': term,
        'searchType': 'image',
        'imgSize': 'large'
    })


def link_search(term):
    return search_call({
        'q': term
    })


def search_call(params):
    params['key'] = SEARCH_KEY
    params['cx'] = SEARCH_CX
    params['alt'] = 'json'
    call_url = SEARCH_URL + '?' + urlencode(params)
    r = requests.get(call_url)
    if r.status_code != 200:
        print r.status_code
        return False
    else:
        return r.json['items']
