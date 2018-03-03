import requests, binascii

URL = 'http://127.0.0.1:5000/test?file=temp&sig='
TIME_LEAK = 0.05
DIFF = 0.02
BYTE_LENGTH = 20

def isValid(sig, rounds):
    #Bytes to hex
    sig = sig.hex()
    #Get time
    time=0
    for i in range(20):
        time += requests.get(URL+sig).elapsed.total_seconds()
    time = time/20
    print(time)
    
    if time>(TIME_LEAK+DIFF)*(rounds+1):
        return True
    else:
        return False

def create_sig():
    valid_sig = b''   
     
    for i in range(BYTE_LENGTH):
        sig = bytes([0])*(BYTE_LENGTH-1-i)
        print(valid_sig)
        for j in range(255):
                        
            if isValid(valid_sig + bytes([j]) + sig, i):
                valid_sig += bytes([j])
                break
            
create_sig()

