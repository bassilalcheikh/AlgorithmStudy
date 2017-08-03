import math
from eratosieve import eratosieve


primes = eratosieve(32)

# target: we want to find primes under square root of 50

#def primeindex(limit, prime_list):
#    upper_limit = math.sqrt(limit)
#    list_length = len(prime_list)
#    if prime_list[list_length/2]

#prime_list = enumerate(primes)


pcount = len(primes)

L = [primes, range(0, pcount)]
X_p = 18
i = 0
while len(L[1]) > 1:
    #print i, len(L[1])
    pcount = len(L[1])
    if L[0][int(pcount/2)] == X_p:
        L[1] = L[1][int(pcount/2)]
        break
    elif L[0][int(pcount/2)] > X_p:
        L[0] = L[0][:int(pcount/2)]
        L[1] = L[1][:int(pcount/2)]
    elif L[0][int(pcount/2)] < X_p:
        L[0] = L[0][int(pcount/2):]
        L[1] = L[1][int(pcount/2):]

print L[1]
