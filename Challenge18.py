#About endian https://www.cs.umd.edu/class/sum2003/cmsc311/Notes/Data/endian.html
#Endian implement https://docs.python.org/3/library/struct.html

from Crypto.Cipher import AES
from struct import pack
import base64, Methods



def ctr(c, nounce, key):
    cipher = AES.new(key, AES.MODE_ECB)
    streamblock = nounce    
    keystream = b''

    while len(c)>len(keystream):
        #QQ = 8x + 8x bytes ->
        #-> b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00'
        keystream += cipher.encrypt(pack('<QQ', nounce ,streamblock))
        #add one to counter each round
        streamblock +=1
    
    #xor keystream with plain or ciphertext
    return Methods.xor(keystream, c)
    


if __name__ == "__main__":
    c = base64.b64decode("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")
    key = b"YELLOW SUBMARINE"

    decrypt = ctr(c, 0, key)
    encrypt = ctr(decrypt, 0, key)


    print(c)
    print(decrypt)
    print(encrypt)