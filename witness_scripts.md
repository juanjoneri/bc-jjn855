# Username & Password Check

Succeeds if username and password match the correct value

Witness Script
```
OP_SWAP
<'username'>
OP_EQUALVERIFY
OP_SHA256
<0x5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8>
OP_EQUAL
```

Stack Elements
```
<'username'>
<'password'>
```
