
def unpadPKCS7(s):
   if bytes([s[-1]])*s[-1] == s[-s[-1]:]:
           #return s[:-s[-1]]
           return True
           
   else:
        return False
    
    


