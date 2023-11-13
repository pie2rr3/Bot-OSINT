import requests

token1 = '0x5565e7344015c0f8f9e6029126f83121055a680b' # adresse du contrat du premier token
token2 = '0x3d2Ec08959Ec20127Bb4578885e2Cd0b2bFc31Fa' # adresse du contrat du deuxième token

startBlock1 = '16765747' # numéro de bloc de début de la plage horaire pour le premier token
endBlock1 = '16766153' # numéro de bloc de fin de la plage horaire pour le premier token
startBlock2 = '16765145' # numéro de bloc de début de la plage horaire pour le deuxième token
endBlock2 = '16765783' # numéro de bloc de fin de la plage horaire pour le deuxième token


apiUrl = 'https://api.etherscan.io/api'
apiKey = 'apikey'

walletFile = 'wallet.txt'



def getTokenTransfers(contractAddress, startBlock, endBlock):
    url = f'{apiUrl}?module=account&action=tokentx&contractaddress={contractAddress}&startblock={startBlock}&endblock={endBlock}&sort=asc&apikey={apiKey}'
    response = requests.get(url)
    return response.json().get('result', [])


def getWallets():
    transfers1 = getTokenTransfers(token1, startBlock1, endBlock1)
    transfers2 = getTokenTransfers(token2, startBlock2, endBlock2)
    
    
    wallets1 = set(t['from'] for t in transfers1)
    wallets2 = set(t['from'] for t in transfers2)
    
    
    wallets = wallets1.intersection(wallets2)
    
    if wallets:
        with open(walletFile, 'w') as f:
            f.write('\n'.join(wallets))
        print(f'{len(wallets)} wallet(s) found and saved in {walletFile}.')
    else:
        print('No wallet found.')

getWallets()
