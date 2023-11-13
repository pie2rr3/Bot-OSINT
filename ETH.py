import requests

token1 = '0x99492eaF5A6b570B409cc8EaB7116939315E487F' # adresse du contrat du premier token
token2 = '0x6f3277ad0782a7DA3eb676b85a8346A100BF9C1c' # adresse du contrat du deuxième token
token3 = '0xB0e977e0214BCfEec0D685064244Ad2b2487380b' # adresse du contrat du troisième token

startBlock1 = '16755852' # numéro de bloc de début de la plage horaire pour le premier token
endBlock1 = '16765413 ' # numéro de bloc de fin de la plage horaire pour le premier token
startBlock2 = '16472767 ' # numéro de bloc de début de la plage horaire pour le deuxième token
endBlock2 = '16762964' # numéro de bloc de fin de la plage horaire pour le deuxième token
startBlock3 = '16751348' # numéro de bloc de début de la plage horaire pour le troisième token
endBlock3 = '16765853' # numéro de bloc de fin de la plage horaire pour le troisième token

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
    transfers3 = getTokenTransfers(token3, startBlock3, endBlock3)
    
    wallets1 = set(t['from'] for t in transfers1)
    wallets2 = set(t['from'] for t in transfers2)
    wallets3 = set(t['from'] for t in transfers3)
    
    wallets = wallets1.intersection(wallets2).intersection(wallets3)
    
    if wallets:
        with open(walletFile, 'w') as f:
            f.write('\n'.join(wallets))
        print(f'{len(wallets)} wallet(s) found and saved in {walletFile}.')
    else:
        print('No wallet found.')

getWallets()
