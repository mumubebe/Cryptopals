from binascii import unhexlify, b2a_base64
def xor(A, B):
    return b''.join(bytes([A[i]^B[i]]) for i in range(len(B)))


s1 = b2a_base64(unhexlify('1c0111001f010100061a024b53535009181c'))
s2 = b2a_base64(unhexlify('686974207468652062756c6c277320657965'))
expected = b2a_base64(unhexlify('746865206b696420646f6e277420706c6179'))

print(xor(s1, s2).hex())
print(expected.hex())
