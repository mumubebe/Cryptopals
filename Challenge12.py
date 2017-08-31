
from random import randint
from Crypto.Cipher import AES
import Challenge7
import os
import Challenge8
import base64 


def oracle(plaintext):   
    s = base64.b64decode(b"Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
    p = plaintext+s    
    return encrypt(p)

  

def encrypt(plain):    
    #Create blocks
    blocks = Challenge7.createBlocks(plain, len(key))        
    obj = AES.new(key, AES.MODE_ECB)
    cipher = b''
    for b in blocks:
        cipher += obj.encrypt(b)
    return cipher
    

#add 1 byte  each round until new block creates.   
def findBlockLength(oracle):
    n1 = len(oracle(bytes([0])))
    i = 1
    while True:
        n2 = len(oracle(bytes([0])*i))
        if n1<n2:
            return n2-n1
        i += 1 

#Check if could find identical blocks in cipher by appending keylength*3 bytes   
def isECB(oracle ,keylength):
    c = oracle(bytes([0])*keylength*3)
    blocks = Challenge7.createBlocks(c, keylength)    
    return 0<len(Challenge8.findDuplicateECB(blocks))




def byteFeed_ECB(oracle):
    blocklength = findBlockLength(oracle)
    if(isECB(oracle, blocklength)):        
        known = b''        
        while True:
            
            #calculates number of bytes to feed into the first block. 
            #Every byte in block is known except the last one
            bytefeed = b'A'*(blocklength - (len(known)%16) -1)  
            
            #encrypts string with bytefeed
            #then get all known bytes + one unknown
            e = oracle(bytefeed)  
            c = e[0:len(bytefeed)+len(known)+1]
            
            #if num of known bytes equals total lenght of cipher from oracle, then finished
            if(len(e) == len(c)):
                return known
            
            #loops through all bytes to find a match for the unknown
            for i in range(256):               
                t = oracle(bytefeed+known+bytes([i]))[0:len(bytefeed)+len(known)+1]    
                
                #round finished if unknown byte match with i
                if t==c:               
                    known +=bytes([i])                                     
                    break
                      
    else:
        print("Not ECB")
   

def start():        
    result = byteFeed_ECB(oracle)
    print(result)    

#init global variable key
key = os.urandom(16)


    

