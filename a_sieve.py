# http://compoasso.free.fr/primelistweb/page/prime/atkin_en.php
# http://compoasso.free.fr/primelistweb/ressource/Atkin3.java
#
# more optimizations to try:
# (1) arrays instead of lists
# (2) (x+1)^2 - (x)^2 = 2*x+1 increment
# (3) whatever this guy is smoking: https://programmingpraxis.com/2010/02/19/sieve-of-atkin-improved/

from math import sqrt
from time import time
t_0 = time()

def atkin_sieve(limit):
    sieve_list = [False]*(limit+1)
    sieve_list[2:4] = (True, True)
    incr_sequence = [2,4] # to be used for increments
    # Part I: preliminary work
    # First loop
    x = 1
    first_bound = sqrt(limit/4) + 1
    while x < first_bound:
        incr_index = 0
        k_1 = 4*x*x
        y = 1 # good
        if x % 3 == 0:
            while True:
                k = k_1 + y**2
                if (k >= limit):
                    break
                else:
                    sieve_list[k] = not sieve_list[k]
                    incr_index += 1
                    y += incr_sequence[(incr_index & 1)]
        else:
            while True:
                k = k_1 + y * y
                if (k >= limit):
                    break
                else:
                    sieve_list[k] = not sieve_list[k]
                    y += 2
        x += 1

    # Second loop
    x = 1
    second_bound = sqrt(limit/3) + 1
    while x < second_bound:
        incr_index = 1
        y = 2
        k_2 = 3*x*x
        while True:
            k = k_2 + y**2
            if k >= limit:
                break
            sieve_list[k] = not sieve_list[k]
            incr_index += 1
            y += incr_sequence[(incr_index & 1)]
        x += 2

    # Third loop
    x = 1
    third_bound = sqrt(limit)
    while x < third_bound:
        k_3 = 3*x*x
        if ((x & 1 == 0)):
            y = 1
            incr_index = 0
        else:
            y = 2
            incr_index = 1
        while y < x:
            k = k_3 - y * y
            if k < limit:
                sieve_list[k] = not sieve_list[k]
            incr_index += 1
            y += incr_sequence[(incr_index & 1)]
        x += 1

    # Part II: Remove the squares of primes (and their multiples)
    r = 5
    r_squared = r**2
    while r_squared < limit:
        if sieve_list[r]:
            for n in range(r_squared, len(sieve_list), r_squared):
                sieve_list[n] = False
        r += 1
        r_squared = r**2
    # Part III: Append everything into a list
    return [x for x, p in enumerate(sieve_list) if p]

#last_prime = atkin_sieve(100000000)#[-1]
#print (len(last_prime), time()-t_0)
#print (last_prime)
