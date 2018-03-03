from flask import Flask, request, abort
from time import sleep
import os, Challenge29, binascii
app = Flask(__name__)

"""
Web server setup for flask
Requires Flask.
Setup:
    pip install Flask
    export FLASK_APP=Challenge31.py
    python -m flask run
"""
@app.route('/test', methods=['GET'])
def validate():    
    #Get file and sig from url as arguments. Example:
    #http://127.0.0.1:5000/test?file=temp&sig=46b4ec586117154dacd49d664e5d63fdc88efb51
    
    #Convert to bytes (x.encode())
    file = request.args.get('file').encode()
    sig = binascii.unhexlify(request.args.get('sig').encode())
    
    print(hmac)
    print(hmac.hex())
    if insecure_compare(hmac, sig):
        return "Yey!"
    else:
        abort(500)

def insecure_compare(hmac, sig):
    
    for i in range(len(hmac)):
        print(hmac[i])
        print(sig[i])
        if hmac[i] == sig[i]:
            sleep(0.05)
        else:
            return False
    return 200
    
    
#Generate random HMAC for server
key = os.urandom(16)
file = b'file'
#Generate HMAC for with SHA1, H(K||M) for server
hmac = Challenge29.Sha1(key+file)
print(hmac)

