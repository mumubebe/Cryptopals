

import os
import Challenge18

key = os.urandom(16)
IV = os.urandom(16)

def prep(inp):
    inp = inp.replace(b";",b"").replace(b"=",b"")
    s1 = b"comment1=cooking%20MCs;userdata="
    s2 = b";comment2=%20like%20a%20pound%20of%20bacon"
    string = s1+inp+s2
    return Challenge18.ctr(string, 0 , key)
    

def validate(c):
    p = Challenge18.ctr(c, 0, key)
    print(p)
    return (b";admin=true;") in p


x = prep(b'ZZZZZZZZZZZZZZZZ:admin<true')
x = x.replace(bytes([x[48]]), bytes([x[48]^1]))
x = x.replace(bytes([x[54]]), bytes([x[54]^1]))
validate(x)