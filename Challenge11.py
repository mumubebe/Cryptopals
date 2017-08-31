
from random import randint
from Crypto.Cipher import AES
import Challenge7
import os
import Challenge10



def oracle(plaintext):
    keylength = 16
    #Random key
    key = os.urandom(keylength)
    
    #Plaintext 'a' with 5 to 10 random bytes on each side
    #By appending random bytes to the plaintext the blocks will look like:
    #[rrrrraaaaaaaaaaa][aaaaaaaaaaaaaaaa][aaaaaaaaaaaaaaaa][rrrrr....]  
    plain = os.urandom(randint(5,10))+plaintext+os.urandom(randint(5,10))        
    return encrypt(plain, key)

   

def encrypt(plain, key):
   
    #Random between AES and CBC encryption
    if(randint(0,1) == 1):
        #Create blocks
        blocks = Challenge7.createBlocks(plain, len(key))
        
        obj = AES.new(key, AES.MODE_ECB)
        cipher = b''
        for b in blocks:
            cipher += obj.encrypt(b)
        return cipher
    else:
        return Challenge10.encrypt_CBC(plain, key, os.urandom(16))



plaintext = b'a'*43
e = oracle(plaintext)
if(e[16:32]==e[32:48]):
    print("ECB!")
else:
    print("CBC!")