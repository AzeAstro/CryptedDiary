from cryptography.fernet import Fernet
from time import sleep
import os
import json
from datetime import datetime

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
            print("Key is valid.")
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
    


def createRecord(key):
    crypter=Fernet(key)
    time=datetime.today().strftime('%Y.%m.%d %H:%M:%S')
    try:
        while True:
            title=input("Enter the title: ")
            if title.split()==[]:
                print("Title can't be empty!\n")
            else:
                break
    except KeyboardInterrupt:
        print("Canceled by user. Exitting...")
        return False
    
    print("Write the context you want. Ctrl+C to stop input.")
    try:
        context=""
        while True:
            part=input()
            context+=part+"\n"
    except KeyboardInterrupt:
        print("Input stopped.")
    
    if context.split()==[]:
        print("Content is completely empty. Nothing to save.")
        return False
    

    record={}
    record['time']=crypter.encrypt(time.encode()).decode()
    record['title']=crypter.encrypt(title.encode()).decode()
    record['context']=crypter.encrypt(context.encode()).decode()
    return record



def dumpRecord(recordFile,record):
    if os.path.isfile(recordFile):
        with open(recordFile,"r") as f:    
            records=json.load(f)
        records.append(record)
        with open(recordFile,"w") as f:
            json.dump(records,f)
        print("Record successfully created. Check records.json file.")
    else:
        print("Record file does not exist. Creating one...")
        with open("records.json","w") as f:
            json.dump([record],f)
        print("Record successfully created. Check records.json file.")




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
                record=createRecord(key.encode())
                if record==False:
                    print("Exitting...")
                else:
                    dumpRecord("records.json",record)
    else:
        while True:
            key=input("Please,enter key (write g if you want to generate a new one): ")
            if key.lower()=="g" or len(key)==44:
                break
            else:
                print("Invalid input.")
        if key=="g":
            key=Fernet.generate_key()
            key=key.decode()
            print(f"Your key: {key}")
            saveKey(key)
            print("Key saved in key.json file.")
        else:
            if checkKey(key.encode()) == False:
                print("Key is not valid. Exitting...")
            else:
                saveKey(key)
                print("Key saved in key.json file.")
        record=createRecord(key.encode())
        if record==False:
            print("Exitting...")
        else:
            dumpRecord("records.json",record)