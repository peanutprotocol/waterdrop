#!/usr/bin/python3

#############################################################################################
# Usage: brownie run scripts/waterdropNFT/deploy.py
#
#
#############################################################################################

from brownie import Waterdrop,  accounts, network, config
from scripts.helpful_scripts import get_publish_source


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    # merkleRoot = 0x22bd6cc328747d5b7b89b8fecae38a7979e93ded08803dc8e51412905fcafce6
    # base_uri = "ipfs://bafybeih56lk6istzo42eie4kpsoengalm73axfhmprylzdaazdhxgs7vmi"
    waterdrop = Waterdrop.deploy(
        # merkleRoot,
        # base_uri,
        {"from": dev},
        publish_source=get_publish_source(),
    )
    return waterdrop
