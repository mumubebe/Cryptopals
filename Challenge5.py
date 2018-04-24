#Implement repeating-key XOR
def repeating_xor(message, key):
    return b''.join(bytes([message[i]^key[i%len(key)]]) for i in range(len(message)))



if __name__ == "__main__": 
    import binascii
    print(binascii.hexlify(repeating_xor(b"Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal", b"ICE")))
