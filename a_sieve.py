http://compoasso.free.fr/primelistweb/ressource/Atkin3.java

from time import time
t_0 = time()
def atkin_sieve(limit):
    sieve_list = [False]*(limit+1)
    sieve_list[2:4] = (True, True)
    # Part I: preliminary work
    # First loop
    x = x_squared = 1
    while 4*x_squared < limit:
        #if x % 3 == 0:
        y = y_squared = 1
        while y_squared < limit:
            n = 4 * x_squared + y_squared
            if n <= limit and n % 12 in (1,5):
                sieve_list[n] = not sieve_list[n]
            y += 1
            y_squared = y**2
        x += 1
        x_squared = x**2

    # Second loop
    x = x_squared = 1
    while 3*x_squared < limit:
        y = 2
        while y*y < limit:
            n = 3 * x_squared + y*y
            if n <= limit and n % 12 == 7:
                sieve_list[n] = not sieve_list[n]
            y += 2
            #y_squared = y**2
        x += 2
        x_squared = x**2

    # Third loop
    x = x_squared = 1
    while x_squared < limit:
        y = y_squared = 1
        while y_squared < limit:
            if x > y:
                n = 3 * x_squared - y_squared
                if n <= limit and n % 12 == 11:
                    sieve_list[n] = not sieve_list[n]
            y += 1
            y_squared = y**2
        x += 1
        x_squared = x**2

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

last_prime = atkin_sieve(10000000)#[-1]
print (len(last_prime), time()-t_0)
