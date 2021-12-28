from brownie.network import account
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENT, getAccount
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest


def test_fund_and_withdraw():
    account = getAccount()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 1
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip("only for local testing")
    account = getAccount()
    fund_me = deploy_fund_me()
    noOwner = accounts[2]
    with pytest.raises(ValueError) or pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": noOwner})
