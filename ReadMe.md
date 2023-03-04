# CryptedDiary
A diary crypter and storing for further reading, sharing securely with key and so on. The motive to write this is my group. I wanna find out which one of them has enough knowledge to decrypt my public crypted diary.



## What does it do?
Simple things. As you write your "dear diary". It stores your diary records encrypted. So, if you lose the key, you won't be able to decrypt your diary records. Never ever.



## How does it work?
It get raw input from user and encrypts it with the key. Key either can be entered manually and then restored for further records or can be selected from existing key in `key.json` file.
  


## Requirements 
1) Python 3
2) `cryptography` library

## Installation:
1) Install Python 3 with Pip.
2) Install `cryptography` library using Pip:
```
pip install cryptography
```
3) Done.


## Usage:
There are 3 scripts you can use:
1) `encrypter.py`
2) `decrypter.py`
3) `decrypt.py`

`ecnrypter.py` - As you suggest from name, it is for creating records and storing encrypted versions of them. Records will be stored in `records.json`. There, for each record, you will see 4 keywords: `time`, `title`, `context`, `full`

`time` - Stores encrypted version of time that record was written.  
`title` - Stores encrypted version of record's title.  
`context` - Stores encrypted version of content that entered by user.  
`full` - Contains all these 3 above in one encrypted version. Prefered to use if you want to share one record with someone else.
  
  

`decrypter.py` - This one is trying to decrypt records using the key. As always, key can either be entered by user manually for decrypting all records or can be selected one that is inside `keys.json`  

`decrypt.py` for decrypting text with given key. Useful for decrpyting record that you recieved with key.  
Everything else will be guided in script themselves.



## Contribution
No need. Really.

## To my group mates:
I don't believe any of you has enough IQ to at least Google it but if you somehow made your way to this place, please, write me in Instagram or WhatsApp. I would like to know who are you.