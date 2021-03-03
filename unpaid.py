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

print(unpaid['data'])
print(resp.text)

strdata = str(unpaid['data'])
listdata = strdata.split(",")
print(listdata[2])
maybe = float(listdata[2])
print('{:.10f}%'.format(maybe)
