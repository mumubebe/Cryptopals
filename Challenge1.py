from binascii import unhexlify, b2a_base64

def hex_to_b64(s):
    return b2a_base64(unhexlify(s))

s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
b64 = hex_to_b64(s)
print(b64)