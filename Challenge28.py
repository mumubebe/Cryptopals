from binascii import hexlify


def Sha1(message):
    # Message needs to be a multiple of 8 bits for this implementation to work
    length = len(message)
    padding = (55 - length) % 64
    message += bytes([1 << 7]) + (0).to_bytes(padding, byteorder='big') + (length * 8).to_bytes(8, byteorder='big')
    blocks = [bytes_to_int(message[64 * i:64 * (i + 1)]) for i in range(len(message) // 64)]
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    f = [f1, f2, f3, f4]
    k = [0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xCA62C1D6]
    for b in blocks:
        chunks = get_message_chunks(b)
        A = h0
        B = h1
        C = h2
        D = h3
        E = h4
        for i in range(80):
            func = f[i // 20]
            konst = k[i // 20]
            A, B, C, D, E = (rotl(A, 5) + func(B, C, D) + E + konst + chunks[i]) & 0xFFFFFFFF, A, rotl(B, 30), C, D
        h0 = (h0 + A) & 0xFFFFFFFF
        h1 = (h1 + B) & 0xFFFFFFFF
        h2 = (h2 + C) & 0xFFFFFFFF
        h3 = (h3 + D) & 0xFFFFFFFF
        h4 = (h4 + E) & 0xFFFFFFFF
    return int_to_bytes((h0 << 128) | (h1 << 96) | (h2 << 64) | (h3 << 32) | h4)


def get_message_chunks(block):
    w = []
    for i in range(16):
        w.append(block & 0xFFFFFFFF)
        block >>= 32
    w = w[::-1]
    for i in range(16, 80):
        w.append(rotl(w[i - 16] ^ w[i - 14] ^ w[i - 8] ^ w[i - 3], 1))
    return w


def bytes_to_int(m):
    num = 0
    for i, b in enumerate(m[::-1]):
        num += b << i * 8
    return num


def int_to_bytes(n):
    b = []
    while n:
        b.append(n % 256)
        n >>= 8
    return bytes(b[::-1])


def rotl(num, bits):
    num = ((num << bits) ^ (num >> (32 - bits))) & 0xFFFFFFFF
    return num


def f1(B, C, D):
    return D ^ (B & (C ^ D))


def f2(B, C, D):
    return B ^ C ^ D


def f3(B, C, D):
    return (B & C) | (B & D) | (C & D)


def f4(B, C, D):
    return B ^ C ^ D


print(hexlify(Sha1(b'a' * 1000000)))
