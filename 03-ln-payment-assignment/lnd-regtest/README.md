# Detailed Instructions for Regtest

Run bitcoin core

---
lnd instance for alice

cd C:\Users\juanj\Documents\Programs\bc-jjn855\03-ln-payment-assignment\lnd-regtest

.\lnd.exe --configfile=alice.conf --bitcoind.dir=D:\Bitcoin

---
lnd wallet for alice

On another terminal

.\lncli.exe --network regtest --rpcserver 127.0.0.1:10009 unlock

.\lncli.exe --network regtest --rpcserver 127.0.0.1:10009 --macaroonpath data/chain/bitcoin/regtest/admin.macaroon newaddress p2wkh

```
{
    "address": "bcrt1q0xfc8fqg00t8y4h72mc7phxqxnuez2lg2j338q"
}
```

---
Send btc alice 

1. use the send feature in bitcoin core

2. Mine 6 blocks

getnewaddress

```
[
  "39a364027871aefb0c1133d729d59ad2bc09fc87328430eccf3e2817a926e4fe"
]
```

generatetoaddress 5 bcrt1qms6lxwdyxwpgfufm2hleayggn3ahzcgfhvse6p


Same for bob

.\lncli.exe --network regtest --rpcserver 127.0.0.1:10010 create

.\lncli.exe --network regtest --rpcserver 127.0.0.1:10010 --macaroonpath data/chain/bitcoin/regtest/admin.macaroon newaddress p2wkh

```
{
    "address": "bcrt1qwtajpxypefgue93hcd7wjl6xgt2ql0klpzxlpj"
}
```

Open a channel

1. get bobs pubkey

```
.\lncli.exe --network regtest --rpcserver 127.0.0.1:10010 --macaroonpath data/chain/bitcoin/regtest/admin.macaroon getinfo

0277c7ffcb3f85285ebe6be5f5a1ac3d4a99d526693bf42b0c02cc8a7c9768ea57
```

Alice peer with bob
```
.\lncli.exe --network regtest --rpcserver 127.0.0.1:10009 --macaroonpath data/chain/bitcoin/regtest/admin.macaroon connect 0277c7ffcb3f85285ebe6be5f5a1ac3d4a99d526693bf42b0c02cc8a7c9768ea57@localhost:9737
{

}
```

Alice open channel with bob
```
C:\Users\juanj\Documents\Programs\bc-jjn855\lnd>.\lncli.exe --network regtest --rpcserver 127.0.0.1:10009 --macaroonpath data/chain/bitcoin/regtest/admin.macaroon openchannel --node_key=0277c7ffcb3f85285ebe6be5f5a1ac3d4a99d526693bf42b0c02cc8a7c9768ea57 --local_amt=1000000
{
        "funding_txid": "88b52080b35d87852ce7cc27105bfc534a41f70a29211f68d7bb9e020f75657d"
}
```

Mine blocks to confirm channel

---
Alice send payment to bob

Bob generate invoice:
```
.\lncli.exe --network regtest --rpcserver 127.0.0.1:10010 --macaroonpath data/chain/bitcoin/regtest/admin.macaroon addinvoice --amt=10000
{
    "r_hash": "7aca319b1b6939ed3331e066cb083570fb30c640e052c86664e5348e3141c822",
    "payment_request": "lnbcrt100u1p3ksjc7pp50t9rrxcmdyu76ve3upnvkzp4wranp3jqupfvsenyu56guv2peq3qdqqcqzpgxqyz5vqsp56hjl6025kpg2e8vm23l4qjgwd4qap4frjg8akpmxsaau54m5azrs9qyyssqk993zf2rthmu80fqpj5lrq6v0w8r9p5gfuqfnrr4u2tvxjum2c49v6q6ffj5jvfey4vcq5xmneeyp8ftm94y5058xefgz57x7rzvmygp3en4yc",
    "add_index": "1",
    "payment_addr": "d5e5fd3d54b050ac9d9b547f50490e6d41d0d523920fdb0766877bca5774e887"
}
```

Make alice pay
```
.\lncli.exe --network regtest --rpcserver 127.0.0.1:10009 --macaroonpath data/chain/bitcoin/regtest/admin.macaroon sendpayment --pay_req=lnbcrt100u1p3ksjc7pp50t9rrxcmdyu76ve3upnvkzp4wranp3jqupfvsenyu56guv2peq3qdqqcqzpgxqyz5vqsp56hjl6025kpg2e8vm23l4qjgwd4qap4frjg8akpmxsaau54m5azrs9qyyssqk993zf2rthmu80fqpj5lrq6v0w8r9p5gfuqfnrr4u2tvxjum2c49v6q6ffj5jvfey4vcq5xmneeyp8ftm94y5058xefgz57x7rzvmygp3en4yc
Payment hash: 7aca319b1b6939ed3331e066cb083570fb30c640e052c86664e5348e3141c822
Description:
Amount (in satoshis): 10000
Fee limit (in satoshis): 500
Destination: 0277c7ffcb3f85285ebe6be5f5a1ac3d4a99d526693bf42b0c02cc8a7c9768ea57
```

Check alice balance
```
.\lncli.exe --network regtest --rpcserver 127.0.0.1:10009 --macaroonpath data/chain/bitcoin/regtest/admin.macaroon channelbalance
{
    "balance": "986530",
    "pending_open_balance": "0",
    "local_balance": {
        "sat": "986530",
        "msat": "986530000"
    },
    "remote_balance": {
        "sat": "10000",
        "msat": "10000000"
    },
    "unsettled_local_balance": {
        "sat": "0",
        "msat": "0"
    },
    "unsettled_remote_balance": {
        "sat": "0",
        "msat": "0"
    },
    "pending_open_local_balance": {
        "sat": "0",
        "msat": "0"
    },
    "pending_open_remote_balance": {
        "sat": "0",
        "msat": "0"
    }
}
```

Check bob balance
```
.\lncli.exe --network regtest --rpcserver 127.0.0.1:10010 --macaroonpath data/chain/bitcoin/regtest/admin.macaroon channelbalance
{
    "balance": "10000",
    "pending_open_balance": "0",
    "local_balance": {
        "sat": "10000",
        "msat": "10000000"
    },
    "remote_balance": {
        "sat": "986530",
        "msat": "986530000"
    },
    "unsettled_local_balance": {
        "sat": "0",
        "msat": "0"
    },
    "unsettled_remote_balance": {
        "sat": "0",
        "msat": "0"
    },
    "pending_open_local_balance": {
        "sat": "0",
        "msat": "0"
    },
    "pending_open_remote_balance": {
        "sat": "0",
        "msat": "0"
    }
}
```
