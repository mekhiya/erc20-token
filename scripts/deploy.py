from brownie import CBToken
from scripts.helpful_script import get_account
from web3 import Web3


def deploy_token():
    # get account
    # deploy token
    account = get_account()
    init_supply = Web3.toWei(1000, "ether")
    token = CBToken.deploy(init_supply, {"from": account})
    print(f"CB Token Deployed at address {token.address}")


def main():
    deploy_token()
