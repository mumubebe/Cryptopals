
from Crypto.Cipher import AES
import Challenge9
import base64 


#Divide string into blocks length
def createBlocks(cipher, length):
    blocks =  [cipher[i:i + length] for i in range(0, len(cipher), length)]
    #Add padding (Challenge 9)
    blocks[-1] = Challenge9.padding(blocks[-1], length)
    return blocks
    
        

if __name__ == '__main__':
    obj = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
    cipher = base64.b64decode(open("Text7.txt").read())
    print(obj.decrypt(cipher))


