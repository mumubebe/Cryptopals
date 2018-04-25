import Methods, math, base64, operator, Challenge3


#Calculate hamming_distance of two strings
def hamming_distance(s1, s2):
    if len(s1) == len(s2):
        #Convert string to bits
        b1 = Methods.byteToBin(s1)
        b2 = Methods.byteToBin(s2)
        #Sum each matching bit               
        return sum([int(b1[i])^int(b2[i]) for i in range(len(b1))])
        
def find_keysize(cipher, guess_from, guess_to):
    distances = {}
    for keysize in range(guess_from, guess_to):
        normalized_distance = 0
        #create different chunks for different keysize-guesses
        chunks = [cipher[j*keysize:keysize*(j+1)] for j in range(math.ceil(len(cipher)/keysize))]
        
        normalized_distance += hamming_distance(chunks[0], chunks[1])/keysize
        normalized_distance += hamming_distance(chunks[2], chunks[3])/keysize
        normalized_distance += hamming_distance(chunks[1], chunks[3])/keysize
        normalized_distance += hamming_distance(chunks[2], chunks[4])/keysize
        normalized_distance += hamming_distance(chunks[0], chunks[4])/keysize
        normalized_distance += hamming_distance(chunks[2], chunks[1])/keysize
        
        
        distances.update({keysize:normalized_distance})
        sorted_x = sorted(distances.items(), key=operator.itemgetter(1))
    print(sorted_x)

def find_key(cipher, keysize):
    chunks = []
    for i in range(keysize):
        chunks.append(b''.join([cipher[k:k+3] for k in range(i, len(cipher), keysize)]))
    print(chunks)   


if __name__ == "__main__": 
    
    cipher = base64.b64decode(open("Text6.txt").read())
    cipher = b"0123456789"
    #find_keysize(cipher,2,40)
    find_key(cipher, 3)
    