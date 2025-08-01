from tronpy import Tron

_client = Tron(network="mainnet")

def get_wallet_info(address: str) -> dict:
    account = _client.get_account(address)
    resources = _client.get_account_resource(address)

    return {
        "address": address,
        "balance_trx": account.get("balance", 0) / 1_000_000,
        "bandwidth_used": resources.get("net_used", 0) + resources.get("free_net_used", 0),
        "bandwidth_limit": resources.get("net_limit", 0) + resources.get("free_net_limit", 0),
        "energy_used": resources.get("energy_used", 0),
        "energy_limit": resources.get("energy_limit", 0),
    }
