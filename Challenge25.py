
from Crypto.Cipher import AES
import Challenge18, os, base64


def edit(ciphertext, key, offset, newtext):
     plaintext=Challenge18.ctr(ciphertext,0,key)
     return Challenge18.ctr(plaintext[:offset]+newtext+plaintext[offset:], 0 ,key)



if __name__ == "__main__": 
     #Import file from Challenge7
     obj = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
     plaintext = obj.decrypt(base64.b64decode(open("Text7.txt").read()))

     key = os.urandom(16)
     cipher = Challenge18.ctr(plaintext, 0, key)
     print(edit(cipher, key, 0, cipher))
     
     ''' the noob way:
         
     plain = b''
     for i in range(len(cipher)):
         target = plaintext[i]
         for j in range(256):
             if edit(cipher, key, i, bytes([j]))[i] == target:
                 plain += bytes([edit(cipher, key, i, bytes([j]))[i]])
         print(plain)
                 
      '''       