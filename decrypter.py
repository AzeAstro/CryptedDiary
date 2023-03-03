from cryptography.fernet import Fernet, InvalidToken
import os
import json
from sys import stdout
from time import sleep

def checkKeyFile():
    if os.path.isfile("key.json"):
        print("Key file found. Checking for key...")
        return True
    else:
        print("Key file is not found. You will need to enter key manually.")
        return False
    

def checkKey(key):
    key=bytes(key)
    if len(key)!=44:
        print("Error!\nKey length can't be different than 44.")
        return False
    else:
        try:
            tester=Fernet(key)
            print("Key is valid.\n")
            return True
        except ValueError:
            print("Invalid key syntax. Please,enter a valid key.")
            return False
        


def saveKey(key):
    with open("key.json","w") as f:
        json.dump({"key":str(key)},f)


def getKey(keyFile):
    with open(keyFile,"r") as f:
        extracted=json.load(f)
    try:
        return extracted['key']
    except KeyError:
        print("File doesn't contain a key.")
        return False
    



def recordPrint(context):
    for char in context:
        if char == "\n" or char == ".":
            stdout.write(char)
            stdout.flush()
            sleep(0.3)
        else:
            stdout.write(char)
            stdout.flush()
            sleep(0.03)


def decode(key,encryptedText):
    try:
        decrypter=Fernet(key)
        return decrypter.decrypt(encryptedText).decode()
    except InvalidToken:
        print("Invalid/Wrong key.")
        return False

def recordDecode(key,record):
    time=decode(key,record['time'])
    title=decode(key,record['title'])
    context=decode(key,record['context'])
    return time,title,context



def selectRecord(key,recordFile):
    with open(recordFile,"r") as f:
        records=json.load(f)
    recordIndex=1
    for record in records:
        try:
            decrypter=Fernet(key)
            time=decrypter.decrypt(record['time'].encode()).decode()
            title=decrypter.decrypt(record['title'].encode()).decode()
            print(f"{recordIndex}) Time: {time}\nTitle: {title}\n")
            recordIndex+=1
        except InvalidToken:
            print("Wrong key or corrupted data. Exitting...")
            return False
    while True:
        selectedRecordIndex=input(f"Enter record index you want to decrypt: ")
        try:
            selectedRecordIndex=int(selectedRecordIndex)
            return records[selectedRecordIndex-1]
        except IndexError:
            print("Enter a valid record number.\n")
        except:
            print("Enter a valid number.\n")
    


if __name__=="__main__":
    print("Welcome to CryptedDiary!")
    print("Looking for key file...")
    if checkKeyFile():
        key=getKey("key.json")
        if key==False:
            print("Valid key not found. Exitting...")
        else:
            if checkKey(key.encode()) == False:
                print("Valid key not found. Exitting...")
            else:
                record=selectRecord(key.encode(),"records.json")
                if record==False:
                    print("Exitting...")
                else:
                    time,title,context=recordDecode(key.encode(),record)
                    recordPrint(f"\nTime: {time}\n")
                    recordPrint(f"Title: {title}\n")
                    recordPrint(f"\n\nContext:\n{context}")
    else:
        while True:
            key=input("Please,enter key (write g if you want to generate a new one): ")
            if len(key)==44:
                break
            else:
                print("Invalid input.")
        if checkKey(key.encode()) == False:
            print("Key is not valid. Exitting...")
        else:
            saveKey(key)
            print("Key saved in key.json file.")
            record=selectRecord(key.encode(),"records.json")
            if record==False:
                print("Exitting...")
            else:
                time,title,context=recordDecode(key.encode(),record)
                recordPrint(f"\nTime: {time}\n")
                recordPrint(f"Title: {title}\n")
                recordPrint(f"\n\nContext:\n{context}")