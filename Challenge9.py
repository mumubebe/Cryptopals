
#Padding inserting byte text
def padding(s, length):
    return s if len(s) == length else s + bytes([length-len(s)%length]*(length-len(s)%length))
    
    
   


