import requests

token1 = '0x21E6bc780bFcd36D36444F68e4962c7cEB255229' # adresse du contrat du premier token
token2 = '0xCCD3891c1452b7CB0E4632774B9365DC4eE24f20' # adresse du contrat du deuxième token

startBlock1 = '69141817' # numéro de bloc de début de la plage horaire pour le premier token
endBlock1 = '69152228' # numéro de bloc de fin de la plage horaire pour le premier token
startBlock2 = '67809815' # numéro de bloc de début de la plage horaire pour le deuxième token
endBlock2 = '67865385' # numéro de bloc de fin de la plage horaire pour le deuxième token


apiUrl = 'https://api.arbiscan.io/api'
apiKey = 'IRFAIKYWS5CIJVS6SH9Z3S998VY6KCEGIP'

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
