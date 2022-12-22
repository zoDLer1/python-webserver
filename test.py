import requests


requests.post('http://localhost/mails', params={'elems':[
    {'mail': 'asdafd', 'password': 'adfsadfd'},
    {'mail': 'asdafd', 'password': 'adfsadfd'},
    {'mail': 'asdafd', 'password': 'adfsadfd'},
    {'mail': 'asdafd', 'password': 'adfsadfd'},
]})