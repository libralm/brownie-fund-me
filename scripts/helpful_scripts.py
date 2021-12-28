from brownie import network, accounts, MockV3Aggregator
from brownie.network import web3
import eth_account
from web3 import Web3

DECIMALS = 8

STARTING_PRICE = 400000000000

LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["eth-mainnet-fork"]


def getAccount():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT
        or FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        # return accounts.add(config["wallets"]["METAMASK_ACCOUNT2_PRIVATE_KEY"])
        return accounts.load("metamast-account2")


def deploy_mock():
    if len(MockV3Aggregator) <= 0:
        mock_aggregator = MockV3Aggregator.deploy(
            DECIMALS, STARTING_PRICE, {"from": getAccount()}
        )
