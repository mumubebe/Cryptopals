import base64, Challenge18
from random import randint
import os




if __name__ == "__main__": 
    key = os.urandom(16)
    string = open("Text19.txt").read().split('\n')
    string = [base64.b64decode(string[i]) for i in range(len(string))]
    ciphers = [Challenge18.ctr(c, 0, key) for c in string]
    
    
    
    
    
    
    