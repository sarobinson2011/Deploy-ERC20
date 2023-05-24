from brownie import OurToken, accounts, config, network


FORKED_LOCAL_NETWORKS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_NETWORKS = ["development", "ganache-local"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_NETWORKS
        or network.show_active() in FORKED_LOCAL_NETWORKS
    ):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])
