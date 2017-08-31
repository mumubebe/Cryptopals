
import os
import Challenge10

key = os.urandom(16)
IV = os.urandom(16)

def prep(inp):
    inp = inp.replace(b";",b"").replace(b"=",b"")
    s1 = b"comment1=cooking%20MCs;userdata="
    s2 = b";comment2=%20like%20a%20pound%20of%20bacon"
    string = s1+inp+s2
    return Challenge10.encrypt_CBC(string, key, IV)
    

def validate(c):
    p = Challenge10.decrypt_CBC(c, key, IV)
    return p.index(b";admin=true;")>0


#Z*16 first block. bitflip first Z to controll the ":" etc.....    
x = prep(b'ZZZZZZZZZZZZZZZZ:admin<true:ZZZZ')
x = x.replace(bytes([x[32]]), bytes([x[32]^1]))
x = x.replace(bytes([x[38]]), bytes([x[38]^1]))
x = x.replace(bytes([x[43]]), bytes([x[43]^1]))

print(validate(x))
