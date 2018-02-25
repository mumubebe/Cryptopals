
import os
import Challenge10

key = os.urandom(16)
IV = key

def prep(inp):
    if is_ascii(inp):
        s1 = b"comment1=cooking%20MCs;userdata="
        s2 = b";comment2=%20like%20a%20pound%20of%20bacon"
        string = s1+inp+s2
        return Challenge10.encrypt_CBC(string, key, IV)
    else:
        raise Exception("Not ASCII")
        

def validate(c):
    p = Challenge10.decrypt_CBC(c, key, IV)
    return p.index(b";admin=true;")>0

def is_ascii(s):
    return all(c < 128 for c in s)

#Z*16 first block. bitflip first Z to controll the ":" etc.....    
x = prep(b'ZZZZZZZZZZZZZZZZ:admin<true:ZZZZ')


print(validate(x))



