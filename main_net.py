from web3 import Web3

with open('api_key/key') as file:
    key = file.read().strip()

url = f'https://mainnet.infura.io/v3/{key}'
my_provider = Web3.HTTPProvider(url)
w3 = Web3(my_provider)

latest_block = w3.eth.get_block('latest')

print(f'Latest block height: {latest_block["number"]}')
print('No. of transactions', len(latest_block['transactions']))

