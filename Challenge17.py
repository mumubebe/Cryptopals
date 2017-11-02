
import base64, os, Challenge10, Challenge15, Challenge7
from random import randint

key = os.urandom(16)
IV = os.urandom(16)
#Function 1
def encr():
    s = base64.b64decode(open("Text17.txt").read().split("\n")[randint(0,9)])
    c = Challenge10.encrypt_CBC(s, key, IV)
    return c

def padding_oracle(c):
    p = Challenge10.decrypt_CBC(c, key, IV)
    return Challenge15.unpadPKCS7(p)

    

def force_blockpair(b1, b2, oracle):
    newb = list(os.urandom(len(b1)))
    known = list()
    
    for char in range(len(b1)):
        for i in range(1, 255):
            #change char until right padding
            newb[-char-1] = i
            #if padding returns true
            if oracle(bytes(newb+list(b2))):
                pad = char+1
                known = [pad^i] + known
                
                #prep for next char
                for x in range(1, pad+1):
                    newb[-x] = known[-x]^(pad+1)
                del newb[:-pad]                
                newb = list(os.urandom(len(b1)-pad)) + newb 
                break
    return bytes([known[i]^b1[i] for i in range(len(known))])
   

def padding_oracle_attack(c, oracle):
    b = Challenge7.createBlocks(c, 16)
    plain = b''
    for i in range(len(b)):
        plain += force_blockpair(IV, b[i], oracle) if i==0  else force_blockpair(b[i-1], b[i], oracle)
        print(i)
    return plain
c = encr()


if __name__ == "__main__":
    print(padding_oracle_attack(c, padding_oracle))








