import json 
from web3 import Web3

infura_url= "Enter Infura URL"
web3=Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

abi = json.loads("abi here")
address = "Contract Address here"

contract = web3.eth.contract(address=address, abi=abi)

totalSupply = contract.functions.totalSupply().call()
print(web3.fromWei(totalSupply, 'ether'))
print(contract.functions.name().call())
print(contract.functions.symbol().call())
balance = contract.functions.balanceOf("Wallet Addresss").call()
print(web3.fromWei(balance, 'ether'))
