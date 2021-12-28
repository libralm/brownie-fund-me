from brownie import IPancakeFactory, accounts, network, config
from scripts.helpful_scripts import getAccount


def deploy_simple_storage():
    # 用brownie 提供的accounts
    account = getAccount()
    # 加载自己在bownie上添加的第三方账户，会让你输入密码（类似于钱包的登陆密码）
    # account = accounts.load("metamast-account2")
    # 根据环境变量来加载账户(两种方法)
    # account = accounts.add(os.getenv("METAMASK_ACCOUNT2_PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["METAMASK_ACCOUNT2_PRIVATE_KEY"])
    # print(account)
    accountkeyValue = {"from": account}
    simple_storage = IPancakeFactory.deploy(accountkeyValue)


def read_all_pairs_length():
    length = IPancakeFactory.allPairsLength()
    print("length:", length)


def main():
    deploy_simple_storage()
