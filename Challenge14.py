import Challenge7, Challenge12, Challenge8
import os
import base64 
from random import randint



def oracle(plaintext):   
    s = base64.b64decode(b"Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
    prefix = os.urandom(randint(16, 32))
    p = prefix+plaintext+s    
    return Challenge12.encrypt(p)


def identifier(oracle, bytestring):
    c = oracle(bytestring*2)
    blocks = Challenge7.createBlocks(c, len(bytestring))
    while len(Challenge8.findDuplicateECB(blocks))==0:
        c = oracle(bytestring*2)
        blocks = Challenge7.createBlocks(c, len(bytestring))
    return Challenge8.findDuplicateECB(blocks)[0]
    

def byteFeed_ECB_wpre(oracle):
    blocklength = 16
    bytestring = os.urandom(blocklength)
    
    #calls the identifier function which keeps tracks of position in ciphertext
    #by appending a block of B*16 we will get a known block
    #by checking each time if and where this block exist it is possible to append the bytefeeding
    checker = identifier(oracle, bytestring)
    inputchecker = b'b'*15+bytestring
    
    
    if(Challenge12.isECB(oracle, blocklength)): 
        print("breaking..")
        known = b''        
        while True:
            #calculates number of bytes to feed into the first block. 
            #Every byte in block is known except the last one
            bytefeed = b'A'*(blocklength - (len(known)%blocklength) -1)  
            
            #encrypts string with bytefeed
            #then get all known bytes + one unknown
            e = b''
            #only if checker-block exist
            while(checker not in e):
                e = oracle(inputchecker+bytefeed)
            
            start = e.index(checker)+blocklength
            stop = len(bytefeed)+len(known)+1
            
            c = e[start : start+stop]
            #if num of known bytes equals total lenght of cipher from oracle, then finished
            if(len(e[start:]) == len(c)):
                return known
            
            #loops through all bytes to find a match for the unknown
            t = b''
            for i in range(256): 
                #only if checker-block exist
                while(checker not in t):
                    t = oracle(inputchecker+bytefeed+known+bytes([i]))
                t = t[start : start + stop] 
                
                #round finished if unknown byte match with i
                if t==c:
                    known +=bytes([i])                                     
                    break
                      
    else:
        raise Exception("Not ECB")



#init global variable key
key = os.urandom(16)

print(byteFeed_ECB_wpre(oracle))
