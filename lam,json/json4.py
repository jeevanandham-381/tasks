import json
import requests
response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#print(type(response))
bitcoininfo=response.json()
print(type(bitcoininfo))
#print(bitcoininfo)
print(bitcoininfo['time']['updated'])
print("in usd:",bitcoininfo['bpi']['USD']['rate'])