
import Challenge7
from Crypto.Cipher import AES
import os

def encrypt(plain):    
    #Create blocks
    blocks = Challenge7.createBlocks(plain, len(key))        
    obj = AES.new(key, AES.MODE_ECB)
    cipher = b''
    for b in blocks:
        cipher += obj.encrypt(b)
    return cipher

def decrypt(cipher):
    obj = AES.new(key, AES.MODE_ECB)
    return obj.decrypt(cipher)

def routine(s):
    s = s.decode("utf-8") 
    k = s.split('&')
    string = "{\n"
    for s in k:
        t = s.split('=')
        string += "'{0}': '{1}',\n".format(t[0], t[1])
    string += "\n}"
    return string
    
def profile_for(user):
    user.replace("&", "").replace("=", "")
    
    string = ("email="+user+"&uid=10&role=user").encode()
    return encrypt(string)



if __name__ == "__main__":   
    key = os.urandom(16)
    user = profile_for('user@mail.com')
    decrypt = decrypt(user)
    print(routine(decrypt))
