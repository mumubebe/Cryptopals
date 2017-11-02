
import Challenge7, Methods
from Crypto.Cipher import AES




def encrypt_CBC(plaintext, key, IV):
    
    keysize = len(key)
    
    #Create blocks containing plaintext
    blocks = Challenge7.createBlocks(plaintext, keysize)      
    
    obj = AES.new(key, AES.MODE_ECB)
    
    #Init IV for XOR first block
    prev = IV
    cipher = b''
    
    for i in range(len(blocks)):
        cipher += obj.encrypt(Methods.xor(blocks[i], prev))
        
        #grab last cipher-part for next xor-round
        prev = cipher[-keysize:]   
    return cipher
    
    
    
    

def decrypt_CBC(cipher, key, IV):
   
    keysize = len(key)        
    obj = AES.new(key, AES.MODE_ECB)
    
    blocks = Challenge7.createBlocks(cipher, keysize)
    plain = b''
    prev = IV
    for i in range(len(blocks)):
        plain += Methods.xor(obj.decrypt(blocks[i]), prev)
        prev = blocks[i]
        
        
    return plain


if __name__ == "__main__":
    key = b"YELLOW SUBMARINE"
    IV = b'\x00'*len(key)
    plaintext = b"YELLOW"

    cipher  = encrypt_CBC(plaintext, key, IV)
    #print(decrypt_CBC(cipher, key, IV))
    #cipher = base64.b64decode(open("Text10.txt").read())
    #print(decrypt_CBC(cipher, key, IV))
   
    