import base64, Challenge18, os

def sort_block(cipherlist):
    
    block = [b'']*len(cipherlist)
    for c in cipherlist:
        print(c[0])
        for i in range(len(c)):
            block[i] += c[i]
      

def solve_block(block):
    pass


if __name__ == "__main__":
    key = os.urandom(16)
    string = open("Text20.txt").read().split('\n')
    string = [base64.b64decode(string[i]) for i in range(len(string))]
    ciphers = [Challenge18.ctr(c, 0, key) for c in string]
    
    block = [c[:16] for c in ciphers]
    print(block)
    sort_block(block)
    