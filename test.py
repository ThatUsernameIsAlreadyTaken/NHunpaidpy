import nicehash
import json
import requests


host = 'https://api2.nicehash.com'
organisation_id = '6802cbfc-7854-4ecb-8526-f6abb1439bb6'
key = '3d13168f-6b85-44aa-bff5-20fb60731031'
secret = '1f6a6143-5cd5-47a9-bf16-1d256d2dc9097d2ece65-ae84-4206-8138-23bbe8d5e4a4' 

private_api = nicehash.private_api(host, organisation_id, key, secret)

accounts = private_api.get_accounts() #get accounts json
accountsdata = str(accounts['total']) #grab totals
accountslist = accountsdata.split("'") #organize
wallet = float(accountslist[7]) #isolate total balance
currencydata = str(accounts['currencies']) #grab currencies
currencylist = currencydata.split(":") #organize
#rate = float('{:.6}'.format(currencylist[270])) #formatting
#total = wallet*rate #make money
#balance = float('{:.2f}'.format(rate)) #drop the digis
#print('{:.14}'.format(currencylist[7]))
print(currencylist)
#print("RVN is currently $"+str(balance)+" USD")