# Detailed Instructions for Testnet

## 1. Run bitcoin core

## 2. lnd instance for alice

cd C:\Users\juanj\Documents\Programs\bc-jjn855\03-ln-payment-assignment\lnd-testnet

.\lnd.exe --configfile=alice.conf --bitcoind.dir=D:\Bitcoin


## 3. lnd wallet for alice

On another terminal

.\lncli.exe --network testnet --rpcserver 127.0.0.1:10009 create

```
---------------BEGIN LND CIPHER SEED---------------
 1. able     2. manage    3. stage     4. student
 5. thumb    6. affair    7. oven      8. sadness
 9. school  10. once     11. loop     12. food
13. word    14. forward  15. habit    16. address
17. aspect  18. half     19. leopard  20. steel
21. shock   22. prize    23. buffalo  24. shy
---------------END LND CIPHER SEED-----------------
```

.\lncli.exe --network testnet --rpcserver 127.0.0.1:10009 --macaroonpath data/chain/bitcoin/testnet/admin.macaroon newaddress p2wkh

```
{
    "address": "tb1qt9ludt378xfdnvrxn3r9997e4mm3uyghpysp63"
}
```

---
## 4. Send 100.000 SATs to alice 

1. use the send feature in bitcoin core

```
Status: 0/unconfirmed, in memory pool
Date: 11/30/2022 22:17
To: tb1qt9ludt378xfdnvrxn3r9997e4mm3uyghpysp63
Debit: -0.00100000 BTC
Transaction fee: -0.00001410 BTC
Net amount: -0.00101410 BTC
Transaction ID: afd8f915d586ee139756f6b20a442ee1294c86cff1ba7f0615483d4a57151724
Transaction total size: 222 bytes
Transaction virtual size: 141 bytes
Output index: 0
```

2. Wait for confirmations


## 5. Same for bob

.\lnd.exe --configfile=bob.conf --bitcoind.dir=D:\Bitcoin

.\lncli.exe --network testnet --rpcserver 127.0.0.1:10010 create

```
---------------BEGIN LND CIPHER SEED---------------
 1. ability    2. wrap     3. reject    4. ride
 5. consider   6. hard     7. slab      8. boss
 9. awake     10. lake    11. weasel   12. clay
13. topple    14. farm    15. fortune  16. sponsor
17. team      18. absorb  19. ability  20. violin
21. time      22. remind  23. state    24. wire
---------------END LND CIPHER SEED-----------------
```

.\lncli.exe --network testnet --rpcserver 127.0.0.1:10010 --macaroonpath data/chain/bitcoin/testnet/admin.macaroon newaddress p2wkh

```
{
    "address": "tb1qjrraz5am8yltzcxgtnsjfzk0nl5y74vvmrzjdq"
}
```

```
Status: 0/unconfirmed, in memory pool
Date: 11/30/2022 22:18
To: tb1qjrraz5am8yltzcxgtnsjfzk0nl5y74vvmrzjdq
Debit: -0.00100000 BTC
Transaction fee: -0.00001410 BTC
Net amount: -0.00101410 BTC
Transaction ID: 73f4b3d324be92d4cd308b28fea190c4ad3aa0705f3a1f2e4fdae5fadb9d8358
Transaction total size: 222 bytes
Transaction virtual size: 141 bytes
Output index: 1
```

Open a channel

1. get bobs pubkey

.\lncli.exe --network testnet --rpcserver 127.0.0.1:10010 --macaroonpath data/chain/bitcoin/testnet/admin.macaroon getinfo

```
"identity_pubkey": "02d90059388cf25dfcd338f0e0f00bcce379a35c6a7c39cec04d6a53b92324ce88"
```

Alice peer with bob
```
.\lncli.exe --network testnet --rpcserver 127.0.0.1:10009 --macaroonpath data/chain/bitcoin/testnet/admin.macaroon connect 02d90059388cf25dfcd338f0e0f00bcce379a35c6a7c39cec04d6a53b92324ce88@localhost:9737
```

Alice open channel with bob
```
.\lncli.exe --network testnet --rpcserver 127.0.0.1:10009 --macaroonpath data/chain/bitcoin/testnet/admin.macaroon openchannel --node_key=02d90059388cf25dfcd338f0e0f00bcce379a35c6a7c39cec04d6a53b92324ce88 --local_amt=20000
```

```
{
        "funding_txid": "88b52080b35d87852ce7cc27105bfc534a41f70a29211f68d7bb9e020f75657d"
}
```

Wait for blocks to confirm channel

---
Alice send payment to bob

Bob generate invoice:
```
.\lncli.exe --network testnet --rpcserver 127.0.0.1:10010 --macaroonpath data/chain/bitcoin/testnet/admin.macaroon addinvoice --amt=10000
{
    "r_hash": "7aca319b1b6939ed3331e066cb083570fb30c640e052c86664e5348e3141c822",
    "payment_request": "lnbcrt100u1p3ksjc7pp50t9rrxcmdyu76ve3upnvkzp4wranp3jqupfvsenyu56guv2peq3qdqqcqzpgxqyz5vqsp56hjl6025kpg2e8vm23l4qjgwd4qap4frjg8akpmxsaau54m5azrs9qyyssqk993zf2rthmu80fqpj5lrq6v0w8r9p5gfuqfnrr4u2tvxjum2c49v6q6ffj5jvfey4vcq5xmneeyp8ftm94y5058xefgz57x7rzvmygp3en4yc",
    "add_index": "1",
    "payment_addr": "d5e5fd3d54b050ac9d9b547f50490e6d41d0d523920fdb0766877bca5774e887"
}
```

Make alice pay
```
.\lncli.exe --network testnet --rpcserver 127.0.0.1:10009 --macaroonpath data/chain/bitcoin/testnet/admin.macaroon sendpayment --pay_req=lnbcrt100u1p3ksjc7pp50t9rrxcmdyu76ve3upnvkzp4wranp3jqupfvsenyu56guv2peq3qdqqcqzpgxqyz5vqsp56hjl6025kpg2e8vm23l4qjgwd4qap4frjg8akpmxsaau54m5azrs9qyyssqk993zf2rthmu80fqpj5lrq6v0w8r9p5gfuqfnrr4u2tvxjum2c49v6q6ffj5jvfey4vcq5xmneeyp8ftm94y5058xefgz57x7rzvmygp3en4yc
Payment hash: 7aca319b1b6939ed3331e066cb083570fb30c640e052c86664e5348e3141c822
Description:
Amount (in satoshis): 10000
Fee limit (in satoshis): 500
Destination: 0277c7ffcb3f85285ebe6be5f5a1ac3d4a99d526693bf42b0c02cc8a7c9768ea57
```

Check alice balance
```
.\lncli.exe --network testnet --rpcserver 127.0.0.1:10009 --macaroonpath data/chain/bitcoin/testnet/admin.macaroon channelbalance
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
.\lncli.exe --network testnet --rpcserver 127.0.0.1:10010 --macaroonpath data/chain/bitcoin/testnet/admin.macaroon channelbalance
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
