
from Crypto.Cipher import AES
import Challenge7
import base64 

#List all duplicates in blocks
def findDuplicateECB(blocks):
    blocks.sort()
    return [blocks[i] for i in range(1, len(blocks)) if blocks[i-1] == blocks[i]]  



                
cipher = base64.b64decode(open("Text8.txt").read())
print(len(findDuplicateECB(Challenge7.createBlocks(cipher,16))))


