## Decrypter for one time usages. Good for decrypting only one record.



from cryptography.fernet import Fernet,InvalidToken
from sys import stdout
from time import sleep

while True:
    key=input("Enter the key: ")
    key=key.encode()
    try:
        decrypter=Fernet(key)
        break
    except:
        print("Invalid key. Please,enter a valid key.\n")


content=input("Enter the content: ")
content=content.encode()
try:
    decrypted=decrypter.decrypt(content)
    decrypted=decrypted.decode()
    print()
    for char in decrypted:
        if char == "\n" or char == ".":
            stdout.write(char)
            stdout.flush()
            sleep(0.3)
        else:
            stdout.write(char)
            stdout.flush()
            sleep(0.03)
except InvalidToken:
    print("Invalid content for key. Either content is corrupted or you use wrong key.")