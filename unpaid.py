import nicehash
import json
import requests

def get_json(endpoint):
    resp = requests.get(endpoint)
    assert resp.status_code == 200
    result = json.loads(resp.content.decode('utf8').replace("'", '"'))
    assert not 'error' in result['result']
    return result

host = 'https://api2.nicehash.com'
organisation_id = 'Organization'
key = 'Public Key'
secret = 'Secret Key' 

private_api = nicehash.private_api(host, organisation_id, key, secret)

unpaid = private_api.get_unpaid()

strdata = str(unpaid['data'])
listdata = strdata.split(",")

maybe = float(listdata[2])
almost = format(float(maybe), '.8f')
working = decimal.Decimal(almost)
final = working * 100000000
print(int(final), "Satoshi")
