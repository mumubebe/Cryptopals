import Methods, math, base64, operator, Challenge3, Challenge5


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
    return sorted_x

def find_key(cipher, keysize):
    #Chunk cipher
    chunks = []
    for i in range(keysize):
        chunks.append(b''.join([cipher[k:k+1] for k in range(i, len(cipher), keysize)]))
    
    #solve each chunk as singel byte xor
    key = b''.join([Challenge3.find_single_byte_key(c) for c in chunks])
    return key

def break_vigenere(cipher, guess_from = 3, guess_to = 30):
    guessed_keysize = find_keysize(cipher,guess_from ,guess_to)
    key = find_key(cipher,guessed_keysize[0][0])
    plain = Challenge5.repeating_xor(cipher, key)
    return plain


if __name__ == "__main__": 
    
    cipher = base64.b64decode(open("Text6.txt").read())
    print(break_vigenere(cipher))
    