# "Sieve of Eratosthenes" by Bassil Alcheikh, 07/11/2016
#
# This standalone function implements a basic Sieve of Eratosthenes algorithm
# that takes some upper bound "n" and returns all primes up to that upper bound
# in the form of a list.

def SieveEratList(n):
    numbers = [False]*2+[True]*(n-2)
    result = []
    for index, prime_candidate in enumerate(numbers):
        if prime_candidate:
            result.append(index)
            for x in xrange(index*index, n, index):
                numbers[x] = False
    return result
