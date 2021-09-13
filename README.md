# security
Repository for keeping track of the quaterly updates related to Grin Community Fund

### Requirements

* Python 3.x
* **[Cryptotools library](https://github.com/mcdallas/cryptotools)**
  * ```pip install git+https://github.com/mcdallas/cryptotools.git@master#egg=cryptotool``` 

**note** running this script requires the use of `Python 3.6` and the installation of the **[Cryptotools library](https://github.com/mcdallas/cryptotools)**:

 #### run security proof script with the security proof file as input, example:
`grin_CC_security_proofs_0.4.py 2021-08-01_security_proof_CC_.txt`

**Run the verifier:** 

```
python3.6 grin_CC_security_proofs_0.4.py 2021-08-01_security_proof_CC_.txt

Transaction: cfbc3792e42a6832825f5b4f9dcb264d7a84662f0365661a05c1db591546bac3
Signature in witness data:     30440220082df4554726abc7427e2426c24e781ff09925acdb849de19943b34039efbcb40220583a4a3dab4bc7499ed5c90fa33e605745801ff7d1d49e7e5bd90cc6caecf9b201
Signature valid: True
Signature in witness data:     304402205673715fff9482c651860d8d4f7aefc38d17286f4309441f90809716b7b0fe8802200cc408680ab4fb19ac96eac8571c546d414195e3f79a8f0e8ba9f5760e445b8b01
Signature valid: True
Signature in witness data:     304402200a214ffd4c7d9ef838b4c892d3e6ff89b0e97715dfda4d3b27955bced7bf2c7b02200d16fa29f771510f772ef79bd4f59bc9bb15770fdb765ba2256db82da3f6a47401
Signature valid: True
Signature in witness data:     3044022076b169949d67b9a122f6527e4f3e311ec5188563be24a9c65c47a04f0191dd3e02201441172e159cb48593ece15aa426c96aaa6a5281bd3a986f95b42ab5f150977201
Signature valid: True
Signature not in witness data: 3044022079d2d40c6fc56dd23fb253934f7f05015002802869b3c0ef8e0b5cc76df9724502200edd25179807bff2cdf20065f69e576c01a13b4c81b893637176684e0cc1cc3701
Signature valid: True
Signature not in witness data: 3044022034be5bcfaccd241c560c743c98d088506b4bc5c02a922348bea983ee1edf23a5022064b3fe8c372cecf739e7dbc8f11959683eebf390287d65ccefb366db8fb4a31301
Signature valid: True

Done, 6 out of 6 signatures in security proof are proven to be valid```
