
from Crypto.Cipher import AES
from Crypto.Util import Counter
import base64

c = base64.b64decode("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")

ctr = Counter.new(128)
cipher = AES.new(b"YELLOW SUBMARINE", AES.MODE_CTR, counter=ctr)
print(cipher.encrypt(c))