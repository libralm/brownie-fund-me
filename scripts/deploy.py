from brownie import FundMe, network, config, MockV3Aggregator
from brownie.network import account, web3
from scripts.helpful_scripts import (
    getAccount,
    deploy_mock,
    LOCAL_BLOCKCHAIN_ENVIRONMENT,
)


def deploy_fund_me():
    account = getAccount()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(fund_me.getPrice())
    return fund_me


def main():
    deploy_fund_me()
