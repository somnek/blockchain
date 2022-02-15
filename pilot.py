# script to mine ethereum

import sys
import json
import requests
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
from eth_account.messages import defunct_hash_message


def get_nonce(web3, address):
    return web3.eth.getTransactionCount(address)


def get_gas_price(web3):
    return web3.eth.gasPrice


def get_gas_limit(web3):
    return web3.eth.getBlock('latest').gasLimit


def get_balance(web3, address):
    return web3.eth.getBalance(address)


def get_block_number(web3):
    return web3.eth.blockNumber


def get_block_hash(web3, block_number):
    return web3.eth.getBlock(block_number).hash


def get_block_timestamp(web3, block_number):
    return web3.eth.getBlock(block_number).timestamp


def get_block_difficulty(web3, block_number):
    return web3.eth.getBlock(block_number).difficulty


# execute
def main():
    # connect to node
    node = 'http://localhost:8545'
    web3 = Web3(HTTPProvider(node))
    web3.middleware_stack.inject(geth_poa_middleware, layer=0)

    # get account
    address = web3.eth.accounts[0]
    nonce = get_nonce(web3, address)
    gas_price = get_gas_price(web3)
    gas_limit = get_gas_limit(web3)
    balance = get_balance(web3, address)
    block_number = get_block_number(web3)
    block_hash = get_block_hash(web3, block_number)
    block_timestamp = get_block_timestamp(web3, block_number)
    block_difficulty = get_block_difficulty(web3, block_number)

    # get the value
    value = int(sys.argv[1])

    # build the transaction
    tx = {
        'from': address,
        'to': address,
        'value': value,
        'gasPrice': gas_price,
        'gas': gas_limit,
        'nonce': nonce
    }

    # sign the transaction
    signed_tx = web3.eth.account.signTransaction(tx, private_key=address)

    # send the transaction
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    # get the receipt
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    # get the tx_id
    tx_id = web3.toHex(web3.sha3(signed_tx.rawTransaction))

    # build the response
    response = {
        'tx_id': tx_id,
        'tx_hash': tx_hash,
        'receipt': receipt,
        'nonce': nonce,
        'gas_price': gas_price,
        'gas_limit': gas_limit,
        'value': value,
        'block_number': block_number,
        'block_hash': block_hash,
        'block_timestamp': block_timestamp,
        'block_difficulty': block_difficulty,
        'balance': balance

    }

    # print the response
    print(json.dumps(response))


if __name__ == '__main__':
    main()
    