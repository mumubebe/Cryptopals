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
        keystream += cipher.encrypt(pack('<QQ', nounce ,streamblock))
        streamblock +=1
    return Methods.xor(keystream, c)
    


c = base64.b64decode("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")
key = b"YELLOW SUBMARINE"

decrypt = ctr(c, 0, key)
encrypt = ctr(decrypt, 0, key)


print(c)
print(decrypt)
print(encrypt)