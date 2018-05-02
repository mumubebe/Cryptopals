import Methods, math, base64, operator, Challenge3, Challenge5


#Calculate hamming_distance of two strings
def hamming_distance(s1, s2):
    if len(s1) == len(s2):
        #Convert string to bits
        b1 = Methods.byteToBin(s1)
        b2 = Methods.byteToBin(s2)
        #Sum each matching bit               
        return sum([int(b1[i])^int(b2[i]) for i in range(len(b1))])
    else:
        assert("String not same size")
        
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
        normalized_distance += hamming_distance(chunks[1], chunks[4])/keysize
        normalized_distance += hamming_distance(chunks[0], chunks[3])/keysize
        normalized_distance += hamming_distance(chunks[2], chunks[1])/keysize
        
        #Put results in list and order
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

#main function
def break_vigenere(cipher, guess_from = 2, guess_to = 30):
    guessed_keysize = find_keysize(cipher,guess_from ,guess_to)
    key = find_key(cipher, guessed_keysize[0][0])
    print(key)
    plain = Challenge5.repeating_xor(cipher, key)
    return plain


if __name__ == "__main__": 
    cipher = b"alp gwcsepul gtavaf, nlv prgpbpsu mb h jcpbyvdlq, ipltga rv glniypfa we ekl 16xs nsjhlcb. px td o lccjdstslpahzn fptspf xstlxzi te iosj ezv sc xcns ttsoic lzlvrmhaw ez sjqijsa xsp rwhr. tq vxspf sciov, alp wsphvcv pr ess rwxpqlvp nwlvvc dyi dswbhvo ef htqtafvyw hqzfbpg, ezutewwm zcep xzmyr o scio ry tscoos rd woi pyqnmgelvr vpm . qbctnl xsp akbflowllmspwt nlwlpcg, lccjdstslpahzn fptspfo oip qvx dfgysgelipp ec bfvbxlrnj ojocjvpw, ld akfv ekhr zys hskehy my eva dclluxpih yoe mh yiacsoseehk fj l gebxwh sieesn we ekl iynfudktru. xsp yam zd woi qwoc."
    print(Challenge5.repeating_xor(cipher, b"helloworld"))
    #cipher = base64.b64decode(open("Text6.txt").read())
    #print(break_vigenere(cipher))
    