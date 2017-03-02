# Sieve of Atkin
#
#
#
# 1. Create a results list, filled with 2, 3, and 5.
# 2. Create a sieve list with an entry for each positive integer; all entries
#    of this list should initially be marked non prime.
# 3. For each entry number n in the sieve list, with modulo-sixty remainder r:
#       (a) If r is 1, 13, 17, 29, 37, 41, 49, or 53, flip the entry for each
#           possible solution to 4(x^2) + y^2 = n.
#       (b) If r is 7, 19, 31, or 43, flip the entry for each possible solution
#           to 3(x^2) + y^2 = n.
#       (c) If r is 11, 23, 47, or 59, flip the entry for each possible
#           solution to 3(x^2) – y^2 = n when x > y.
#       (d) If r is something else, ignore it completely.
# 4. Start with the lowest number in the sieve list.
# 5. Take the next number in the sieve list still marked prime.
# 6. Include the number in the results list.
# 7. Square the number and mark all multiples of that square as non prime. Note
#    that the multiples that can be factored by 2, 3, or 5 need not be marked,
#    as these will be ignored in the final enumeration of primes.
# 8. Repeat steps four through seven.
# ==============================================================================
def atkin_sieve(limit):
    sieve_list = [-1]*limit
    sieve_list[2] *= -1
    sieve_list[3] *= -1
    x = 1
    while(x*x < limit):
        y = 1
        while(y*y < limit):
            n = (4*x*x)+(y*y)
            if n <= limit and (n%12==5 or n%12==1):
                sieve_list[n] *= -1

            n = (3*x*x)+(y*y)
            if n <= limit and n%12==7:
                sieve_list[n] *= -1

            n = (3*x*x)-(y*y)
            if n <= limit and n%12==11 and x>y:
                sieve_list[n] *= -1

            y += 1
        x += 1

    r = 5
    while r*r < limit:
        if sieve_list[r] > 0:
            i = r*r
            while i*i < limit:
                sieve_list[i] *= -1
                i += r*r
        r += 1

    results = []
    x = 0
    for p in sieve_list:
        if p > 0:
            results.append(x)
        x += 1

    return results

print(atkin_sieve(200))


# http://www.geeksforgeeks.org/sieve-of-atkin/
