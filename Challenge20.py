import base64, Challenge18, os, Methods


def solve_block(block):
    score = 0
    key = bytes([0])
    #loop every possible key¨¨    
    for i in range(256):          
        #xor cipher w possible key and generate a string
        s = ''.join([chr(ord(c)^i) if c not in b'' else '' for c in block])
        #Store highest score
        if Methods.score(s) > score:
            score = Methods.score(s)
            key = bytes([i])
    return key
        


if __name__ == "__main__":
    #Prepare key
    rkey = os.urandom(16)
    s = open("Text20.txt").read().split('\n')
    #Base64 decode
    s = [base64.b64decode(s[i]) for i in range(len(s))]
    #Encrypt ctr
    ciphers = [Challenge18.ctr(c, 0, rkey) for c in s]
    
            
    target = ciphers[44]       
    key = b''
    #Solving each character in every string
    for i in range(len(target)-1):
            key += solve_block([c[i:i+1] if (len(c)-1)>=i else b'' for c in ciphers])       
    print(Methods.xor(target, key))
  