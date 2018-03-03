from random import randint
p = 37
g = 5
a = randint(1,9999)%37
A = (g**a) % p
b = randint(1, 9999)%37
B = (g**b) % p

s = (B**a) % p
s1 = (A**b) % p
print (s)
print (s1)

