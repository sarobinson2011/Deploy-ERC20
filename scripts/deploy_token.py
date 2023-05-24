from os import access
from brownie import OurToken, accounts, network, config
from scripts.helpful_scripts import get_account
from web3 import Web3


initial_supply = Web3().toWei(1000, "ether")


def main():
    account = get_account()
    our_token = OurToken.deploy(initial_supply, {"from": account})
    print(
        f"--> {our_token.name()} successfully deployed --> token symbol: {our_token.symbol()}\n"
    )
    print(f"Total supply of {our_token.symbol()} = {our_token.totalSupply()}\n")
