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
.\lncli.exe --network testnet --rpcserver 127.0.0.1:10009 --macaroonpath data/chain/bitcoin/testnet/admin.macaroon openchannel --node_key=02d90059388cf25dfcd338f0e0f00bcce379a35c6a7c39cec04d6a53b92324ce88 --local_amt=25000
```

```
{
        "funding_txid": "a9dcfd30edace911f32e5ae80ce5bc1a40a0a87f562a9c23c5c59235e0f83906"
}
```

Wait for blocks to confirm channel

---
Alice send payment to bob

Bob generate invoice:
```
.\lncli.exe --network testnet --rpcserver 127.0.0.1:10010 --macaroonpath data/chain/bitcoin/testnet/admin.macaroon addinvoice --amt=10000

```
{
    "r_hash": "15800846112eb2a8f16e77bef3a93bdaafee133bb7d4d2e8cafa24b00705cd4d",
    "payment_request": "lntb100u1p3csd9cpp5zkqqs3s396e23utww7l082fmm2h7uyemkl2d96x2lgjtqpc9e4xsdqqcqzpgxqyz5vqsp5wf408wgc4a6yt8mfm582h3xtaylypjxlnuk8w8kgg0f0d32055ps9qyyssqvmuy0glfvquz8kmq4w0n8gdkd97afks9z2529pdjcg5jxquwxtmn6ngvx9m6n2vylmts02zx3htzsmkkpcfwz43kwmsdgrq4g2c3w7qqlw9cee",
    "add_index": "3",
    "payment_addr": "726af3b918af74459f69dd0eabc4cbe93e40c8df9f2c771ec843d2f6c54fa503"
}
```

Make alice pay
```
.\lncli.exe --network testnet --rpcserver 127.0.0.1:10009 --macaroonpath data/chain/bitcoin/testnet/admin.macaroon sendpayment --pay_req=lntb100u1p3csd9cpp5zkqqs3s396e23utww7l082fmm2h7uyemkl2d96x2lgjtqpc9e4xsdqqcqzpgxqyz5vqsp5wf408wgc4a6yt8mfm582h3xtaylypjxlnuk8w8kgg0f0d32055ps9qyyssqvmuy0glfvquz8kmq4w0n8gdkd97afks9z2529pdjcg5jxquwxtmn6ngvx9m6n2vylmts02zx3htzsmkkpcfwz43kwmsdgrq4g2c3w7qqlw9cee
```

```
{
    "payment_hash": "15800846112eb2a8f16e77bef3a93bdaafee133bb7d4d2e8cafa24b00705cd4d",
    "value": "10000",
    "creation_date": "1669871167",
    "fee": "0",
    "payment_preimage": "0000000000000000000000000000000000000000000000000000000000000000",
    "value_sat": "10000",
    "value_msat": "10000000",
    "payment_request": "lntb100u1p3csd9cpp5zkqqs3s396e23utww7l082fmm2h7uyemkl2d96x2lgjtqpc9e4xsdqqcqzpgxqyz5vqsp5wf408wgc4a6yt8mfm582h3xtaylypjxlnuk8w8kgg0f0d32055ps9qyyssqvmuy0glfvquz8kmq4w0n8gdkd97afks9z2529pdjcg5jxquwxtmn6ngvx9m6n2vylmts02zx3htzsmkkpcfwz43kwmsdgrq4g2c3w7qqlw9cee",
    "status": "IN_FLIGHT",
    "fee_sat": "0",
    "fee_msat": "0",
    "creation_time_ns": "1669871167920987400",
    "htlcs": [
    ],
    "payment_index": "5",
    "failure_reason": "FAILURE_REASON_NONE"
}
```

Check alice balance
```
.\lncli.exe --network testnet --rpcserver 127.0.0.1:10009 --macaroonpath data/chain/bitcoin/testnet/admin.macaroon channelbalance
{
    "balance": "9056",
    "pending_open_balance": "24056",
    "local_balance": {
        "sat": "9056",
        "msat": "9056000"
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
        "sat": "24056",
        "msat": "24056000"
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
        "sat": "9056",
        "msat": "9056000"
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
        "sat": "24056",
        "msat": "24056000"
    }
}
```

Alice close channel

```
.\lncli.exe --network testnet --rpcserver 127.0.0.1:10009 --macaroonpath data/chain/bitcoin/testnet/admin.macaroon closechannel --funding_txid=a9dcfd30edace911f32e5ae80ce5bc1a40a0a87f562a9c23c5c59235e0f83906 --force
```

```
{
        "closing_txid": "70ad48b49f4320f4d068527c602a58e605b090371d69d941cc9ea0f2e52c55c5"
}
```