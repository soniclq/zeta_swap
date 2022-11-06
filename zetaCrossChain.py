from audioop import add
from sys import hash_info
from eth_typing import HexStr
from eth_utils import to_hex
from web3 import Web3, HTTPProvider

import json
from util.jsonUtil import jsonUtil


rpc_dict = jsonUtil.load_json("config/rpcs.json")
zeta_token_abi_dict = jsonUtil.load_json("config/zeta_token_abi.json")
zeta_swap_contract_dict=jsonUtil.load_json("config/zeta_swap_abi.json")



rpc = rpc_dict['polygon_mumbai']


web3 = Web3(HTTPProvider(rpc))


def balanceCheck(address):
    balance = web3.fromWei(web3.eth.getBalance(address), "ether")
    return balance


#合约调用
zeta_token_contract = Web3.toChecksumAddress(zeta_token_abi_dict['contract'])
zeta_contract_abi = json.loads(zeta_token_abi_dict['abi'])

zeta_swap_contract = Web3.toChecksumAddress(zeta_swap_contract_dict['contract'])
zeta_swap_contract_abi = json.loads(zeta_swap_contract_dict['abi'])



def  approveZeta(private_key,address):
    web3 = Web3(HTTPProvider(rpc))
    zetaContract = web3.eth.contract(
        address=zeta_token_contract, abi=zeta_contract_abi)
    #approve
    approve_zeta=zetaContract.functions.approve(
        Web3.toChecksumAddress("0xaf28cb0d9E045170E1642321B964740784E7dC64"),
        3000000000000000000
    )
    
    nonce1 = web3.eth.getTransactionCount(address)
    
    gas=web3.eth.gasPrice
    print(gas)
    params = {
    "from": address,
    "value": web3.toWei(0.0000, 'ether'),
    'gasPrice': gas,
    "gas": 500000,
    "nonce": nonce1,
    }
        
    try:
     tx = approve_zeta.buildTransaction(params)
     signed_tx = web3.eth.account.sign_transaction(tx, private_key=private_key)
     tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
     print(f"交易发送成功：{tx_hash.hex()}")
    except Exception as e:
     print(f"{address}交易发送失败：", e)
     
     
     
 #swap    
def testContract(private_key,address):

    swapContract=web3.eth.contract(
        address=zeta_swap_contract, abi=zeta_swap_contract_abi)
    
    #swap
    swap_zeta_matic_to_eth=swapContract.functions.swapTokensForTokensCrossChain(
        Web3.toChecksumAddress("0x000080383847bD75F91c168269Aa74004877592f"),
        3000000000000000000,
        Web3.toChecksumAddress(address),
        Web3.toChecksumAddress("0xCc7bb2D219A0FC08033E130629C2B854b7bA9195"),
        False,
        0,
        5,
        350000
        )
    nonce = web3.eth.getTransactionCount(address)
    
    gas=web3.eth.gasPrice
    params = {
    "from": address,
    "value": web3.toWei(0.0000, 'ether'),
    'gasPrice': gas,
    "gas": 500000,
    "nonce": nonce,
    }
    
    try:
     tx = swap_zeta_matic_to_eth.buildTransaction(params)
     signed_tx = web3.eth.account.sign_transaction(tx, private_key=private_key)
     tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
     print(f"交易发送成功：{tx_hash.hex()}")
     return tx_hash.hex()
    except Exception as e:
     print(f"{address}交易发送失败：", e)




