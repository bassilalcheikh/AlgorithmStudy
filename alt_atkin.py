# https://programmingpraxis.com/2010/02/19/sieve-of-atkin-improved/

from math import sqrt
from time import time

t_0 = time()

def atkins13(limit):
    primes = [0] * limit
    # FIRST LOOP: n = 4x^2 + y^2 section
    x_1 = 0
    for dx_1 in range( 4, 8*int(sqrt((limit - 1 )/4)) + 4, 8 ):
        x_1 += dx_1
        n = x_1+1

        if x_1 % 3:
            for dn in range( 0, 4*int( sqrt( limit - x_1 ) ) - 3, 8 ):
                n += dn
                primes[n] = not primes[n]
        else:
            y_limit = 12 * int( sqrt( limit - x_1 ) ) - 36

            n = x_1 + 25
            for dn in range( -24, y_limit + 1, 72 ):
                n += dn
                primes[n] = not primes[n]

            n = x_1+1
            for dn in range( 24, y_limit + 1, 72 ):
                n += dn
                primes[n] = not primes[n]

    # SECOND LOOP: n = 3x^2 + y^2 section
    x_2 = 3
    for dx_2 in range( 0, 12*int( sqrt( ( limit - 1 ) / 3 ) ), 24 ):
        x_2 += dx_2
        y_limit = int(12*sqrt(limit - x_2) - 36)
        n = x_2 + 16
        for dn in range( -12, y_limit + 1, 72 ):
            n += dn
            primes[n] = not primes[n]

        n = x_2 + 4
        for dn in range( 12, y_limit + 1, 72 ):
            n += dn
            primes[n] = not primes[n]

    # THIRD LOOP: n = 3x^2 - y^2 section
    x_3 = 1
    for x in range( 3, int( sqrt( limit / 2 ) ) + 1, 2 ):
        x_3 += 4*x - 4
        n = 3*x_3

        if n > limit:
            min_y = ((int(sqrt(n - limit))>>2)<<2)
            yy = min_y*min_y
            n -= yy
            s = 4*min_y + 4

        else:
            s = 4

        for dn in range( s, 4*x, 8 ):
            n -= dn
            if n <= limit and n%12 == 11:
                    primes[n] = not primes[n]

    x_3 = 0
    for x in range( 2, int( sqrt( limit / 2 ) ) + 1, 2 ):
        x_3 += 4*x - 4
        n = 3*x_3

        if n > limit:
            min_y = ((int(sqrt(n - limit))>>2)<<2)-1
            yy = min_y*min_y
            n -= yy
            s = 4*min_y + 4

        else:
            n -= 1
            s = 0

        for dn in range( s, 4*x, 8 ):
            n -= dn
            if n <= limit and n%12 == 11:
                    primes[n] = not primes[n]

    # eliminate squares
    for n in range(5,int(sqrt(limit))+1,2):
        if primes[n]:
            for k in range(n*n, limit, n*n):
                primes[k] = False

    return [2,3] + filter(primes.__getitem__, range(5,limit,2))


print(len(atkins13(100000000)), time()-t_0)
