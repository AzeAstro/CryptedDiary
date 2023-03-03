# from cryptography import fernet
# while True:
#     key=fernet.Fernet.generate_key()
#     print(f"Key: {str(key)}\nLen: {len(key)}")


# Key is always 44 bytes length.




# from time import sleep
# from sys import stdout

# testText="""
# Test  Test Test Test Test Test Test Test Test.
# Test Test Test Test Test.
# Test.
# """


# while True:
#     for char in testText:
#         if char == "\n" or char == ".":
#             stdout.write(char)
#             stdout.flush()
#             sleep(0.3)
#         else:
#             stdout.write(char)
#             stdout.flush()
#             sleep(0.03)

# Best sleep time for regular chars is 0.03, best pause time is 0.3
# Output gonna be displayed with sys library.






# from cryptography import fernet

# key=fernet.Fernet.generate_key()
# print(f"Key: {str(key)}\nLen: {len(key)}")

# crypter=fernet.Fernet(key)
# crypted=crypter.encrypt(b"Test")

# key2=fernet.Fernet.generate_key()
# crypter2=fernet.Fernet(key2)
# crypter2.decrypt(crypted)


# Wrong key exception: cryptography.fernet.InvalidToken









# from datetime import datetime
# print(datetime.today().strftime('%Y.%m.%d %H:%M:%S'))


# Time :D





# Test key: b'rXF269anDjlbsjBHWRqApuX4651BEDUNKksiqBRovXk='