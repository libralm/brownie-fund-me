from brownie import FundMe
from brownie.network import accounts
from scripts.helpful_scripts import getAccount


def fund():
    fund_me = FundMe[-1]
    account = getAccount()
    entrace_fee = fund_me.getEntranceFee() + 0.1
    fund_me.fund({"from": account, "value": entrace_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = getAccount()
    fund_me.withdraw({"from": account})


def accountFinance():
    print(accounts[1].balance())


def main():
    # fund()
    # withdraw()
    accountFinance()
