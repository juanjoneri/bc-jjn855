"""
Simple python rpc script derived from
https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line/blob/master/18_4_Accessing_Bitcoind_with_Python.md

Requires bitcoin conf file set up with username=bitcoin password=password.
Use https://jlopp.github.io/bitcoin-core-rpc-auth-generator/ to generate config value

To use with windows powershell

python3 -m venv myenf
.\myenv\Scripts\activate
pip install python-bitcoinrpc
"""


from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from pprint import pprint
import logging

logging.basicConfig()
logging.getLogger("BitcoinRPC").setLevel(logging.DEBUG)
# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_user = "bitcoin"
rpc_pass = "password"
rpc_host = "127.0.0.1" # "192.168.1.193"
rpc_client = AuthServiceProxy(f"http://{rpc_user}:{rpc_pass}@{rpc_host}:18443", timeout=120)

block_count = rpc_client.getblockcount()
print("---------------------------------------------------------------")
print("Block Count:", block_count)
print("---------------------------------------------------------------\n")