import requests, binascii

URL = 'http://127.0.0.1:5000/test?file=temp&sig='
TIME_LEAK = 0.005
BYTE_LENGTH = 20

#Ugliest code ever. Loops through every byte and compares the highest and second highest time value.
def getAvgTime(valid_sig, siglength):
    print(valid_sig)
    time = [0.0]*255
    sortedtime = sorted(time)
    while sortedtime[-1]<(sortedtime[-2]+TIME_LEAK*15):
        for i in range(255):
            time[i] += requests.get(URL+(valid_sig + bytes([i]) + bytes([0])*(BYTE_LENGTH-1-siglength)).hex()).elapsed.total_seconds()
        sortedtime = sorted(time)
    valid_sig += bytes([time.index(sortedtime[-1])])
    getAvgTime(valid_sig, siglength+1)
    
    
            
print(getAvgTime(b"", 0))

