import json
import pprint
import requests
def dcard():
	url = 'https://www.dcard.tw/_api/'
	ping = requests.get(url+'_ping')

	payload = {
	    "email": input('請輸入帳號:'),
	    "password": input('請輸入密碼:')
	}
	headers = {
	    'authority':'www.dcard.tw',
	    'method': 'POST',
	    'content-type': 'application/json',
	    'accept': 'application/json',
	    'x-csrf-token':ping.headers['x-csrf-token']
	}

	r = requests.post(url+'sessions',headers=headers,json=payload,cookies=dict(ping.cookies))
	if r.status_code != 204:
	    print ('登入失敗')
	    return
	cookies = dict(r.cookies)

	d = requests.get(url+'dcard',cookies=cookies)

	pprint.pprint(json.loads(d.text))
dcard()
