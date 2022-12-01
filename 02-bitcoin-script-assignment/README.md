# Assignment 02 - Bitcoin Script

Name    : Juan Neri  
Email   : juanjo.neri@gmail.com  
Discord : juanjoneri#0274  

## Username & Password Check

Succeeds if username and password match the correct value

### Witness Script
```
OP_SWAP
<'username'>
OP_EQUALVERIFY
OP_SHA256
<0x5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8>
OP_EQUAL
```

### Stack Elements
```
<'username'>
<'password'>
```

## Username & Password Check with Salted Hash

Succeeds if username and password match the correct value. Increases security by salting the password hash.

### Witness Script
```
OP_SWAP
<'username'>
OP_EQUALVERIFY
<'salt'>
OP_CAT
OP_SHA256
<0x7a37b85c8918eac19a9089c0fa5a2ab4dce3f90528dcdeec108b23ddf3607b99>
OP_EQUAL
```

### Stack Elements
```
<'username'>
<'password'>
```
