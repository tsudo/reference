# THE Windows GPG CLI CHEATSHEET

---
Last Updated: **20210426**

---
### Key ID's
The majority of these commands require you to specifiy the key to act upon. That is done via a KEY ID. The Key ID is *usually* expressed by name, long ID (aka fingerprint), or short ID.They are interchangeable. Examples:
* torbrowser@torproject.org
* 0x4E2C6E8793298290
* 0xEF6E286DDA85EA2A4BA7DE684E2C6E8793298290

## Import / Export

#### Import Public Key via specified keyserver

Note that the :80 at the end of the server address specifies HTTP as the outbound port and will often resolve issues. It is  advisable to use the long Key ID (fingerprint) when searching or importing keys from a keyserver.
`gpg --keyserver keys.riseup.net --recv-key 0xEF6E286DDA85EA2A4BA7DE684E2C6E8793298290`

`gpg --keyserver sks-keyservers.net:80 --recv-key 0xEF6E286DDA85EA2A4BA7DE684E2C6E8793298290`

`gpg ---keyserver x-hkp://pool.sks-keyservers.net --recv-keys 0x4E2C6E8793298290`

#### Import a Public Key
`gpg --import public.key`

This adds the public key in the file "public.key" to your public key ring.

#### Export/Backup Public Key
`gpg --armor --export alice@cyb.org`
`gpg --armor --export 0x4E2C6E8793298290 > filename.key`
`gpg --armor --export 0x4E2C6E8793298290 > filename.gpg`
`gpg --armor --export 0x4E2C6E8793298290 > filename.txt`


#### Export/Backup PRIVATE key:
`gpg --armor --export-secret-key 0x4E2C6E8793298290  > filename.key`

`gpg --armor --export-secret-key 0x4E2C6E8793298290  > filename.gpg`

`gpg --armor --export-secret-key 0x4E2C6E8793298290  > filename.txt`


#### Export/Backup PRIVATE SUBkey(s):
`gpg --export-secret-subkeys 0x4E2C6E8793298290 > filename.key`

#### Export Trust values:
`gpg --export-ownertrust > filename.txt`

## Fingerprints
#### See Key Fingerprint
`gpg --fingerprint KEYID`

####  Get fingerprint of an on-disk armored key without importing it
`gpg --with-fingerprint [filename.key or filename.asc]`

## Signing Keys and Files
#### See who has trusted (signed) a key
`gpg --list-sigs 0xEF6E286DDA85EA2A4BA7DE684E2C6E8793298290`

#### Verify a signed file
Notes: Put both the file and the signature file (.asc) in the same folder. You'll want to import the public key prior to running the verification.
`gpg --verify file.exe.asc file.exe`

`gpg --verify file.exe.sig file.exe`

Output should say "Good signature from..." & "Signature made DATE by KEYID", don't worry about the warning about the trusted signature. That is related to the trust level of the Key not the validity of the signature.

#### Create a signed file (detached)
This is best for signing a binary/executable file as it creates a new (detached) .sig signature file
`gpg --detach-sign filename`

## Key Management
#### Change the passphrase of the secret key
`gpg --edit-key YOUR_KEYID_HERE`
`gpg> passwd`
`gpg> save`

#### Trust a key
`gpg --edit KEYID`
`gpg> trust`
`gpg> (choose lvl 1-5)`
`gpg> quit`

#### Delete a public key (from your public key ring):
`gpg --delete-key KEYID`

This removes the public key from your public key ring.
NOTE! If there is a private key on your private key ring associated with this public key, you will get an error! You must delete your private key for this key pair from your private key ring first.

#### Delete an private key (a key on your private key ring):
`gpg --delete-secret-key KEYID`

This deletes the secret key from your secret key ring.

## List Keys
#### List the keys in your public key ring:
`gpg --list-keys`

#### List the keys in your *secret* key ring:
`gpg --list-secret-keys`

## REVOCATION
4 steps to revoking your GPG key and publishing the revocation.
1. **Create a Revocation Key**
`gpg --gen-revoke KEYID`

2. **Copy Revocation Key**
You're asked if you want to provide a reason for the revocation (key comprised, superseded or no longer used) and an optional free-text description. After supplying your passphrase, an ascii-armoured key block is printed out. Paste this text into a file

3. **Locally import Revocation key**
`gpg --import my_revocation.txt`

4. **Upload Revocation Key**
`gpg --keyserver pgp.mit.edu --send-keys 0x4E2C6E8793298290`

## ENCRYPT / DECRYPT
#### To encrypt data, use:
Simple version
`gpg --encrypt --recipient 'myfriend@his.isp.net' foo.txt`

Using Options
`gpg --encrypt --u "Sender User Name" --recipient "Receiver User Name" somefile`
-6
There are some useful options here, such as -u to specify the secret key to be used, and -r to specify the public key of the recipient.
As an example: gpg -e -u "Charles Lockhart" -r "A Friend" mydata.tar


#### To decrypt data, use:
`gpg -d mydata.tar.gpg`
OR
`gpg --output foo.txt --decrypt foo.txt.gpg`

If you have multiple secret keys, it'll choose the correct one, or output an error if the correct one doesn't exist. You'll be prompted to enter your passphrase. Afterwards there will exist the file "mydata.tar", and the encrypted "original," mydata.tar.gpg.

---
Compilied by **[@tsudo](https://twitter.com/tsudo)** 

GPG Fingerprint: 95E3 8B55 9E9F 15BA AF41 CFB7 4390 FB8A C4C5 3435
[Public Key](https://keithcrawford.me/gpg/)

Credits: [Madboa](https://www.madboa.com/geek/gpg-quickstart/), [GnuPG Mini Howto](http://www.dewinter.com/gnupg_howto/english/GPGMiniHowto.html), Riseup.net, [chrisroos](https://gist.github.com/chrisroos/1205934), [Alex Cabal](https://alexcabal.com/creating-the-perfect-gpg-keypair/), [Matt Biddulph](https://www.hackdiary.com/2004/01/18/revoking-a-gpg-key/) & [Scout3801](http://irtfweb.ifa.hawaii.edu/~lockhart/gpg/gpg-cs.html)
