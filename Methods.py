freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182 
}




def byteToBin(byte):
    return ''.join(bin(b)[2:].zfill(8) for b in byte)

def binToAscii(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def intToBin(inte):
     return ''.join(bin(i)[2:].zfill(8) for i in inte)

def asciiToBin(s):
    return ''.join(bin(ord(i))[2:].zfill(8) for i in s)

def score(b):
    score = 0
    s = b.lower()
    for i in s:
        if i in freqs:
            score += freqs[i]
    return score

    

def getSingleCharByteList(n):
    return [list(i)*(int(n)) for i in itertools.product(["0", "1"], repeat=8)]
    
def hammingDistance(b1, b2):
    if len(b1) == len(b2):
        hd = 0
        for i in range(len(b1)):
            hd +=0 if b1[i] == b2[i] else 1
        return hd
    else:
        print("Error: binary not in same lenght. Binary 1: "+str(len(b1))+" Binary 2: "+ str(len(b2)))
        
def hexToBin(hex):
    return bin(int(hex, 16))[2:].zfill(len(hex) * 4)

def encrypt_xor(t, k):
    text = intToBin(t)
    #text = asciiToBin(t)
    key = ''
    for i in range(len(t)):
        key += intToBin(k[i%len(k)])
        
    
    return binToHex(xor(key, text))
    

    

def binToHex(bin):
    return hex(int(bin, 2))[2:]


#Byte values
def xor(A, B):
    return b''.join(bytes([A[i]^B[i]]) for i in range(len(B)))

#s1 = hexToBin("1c0111001f010100061a024b53535009181c")

#s2 = hexToBin("686974207468652062756c6c277320657965")


#print(binToHex(xor(s1, s2)))




#print(stringlist)
