# returns primes less than num

import time
import bisect
    def allPrimes(num):
        numberlist = list(range(1,(num+1)))
        p = 1
        notprimelist = list()
        while p != max(numberlist):
            p_index = bisect.bisect_right(numberlist, p)
            p = numberlist[p_index]
            for i in range(2*p, (num+1), p):
                notprimelist.append(i)
        primes = list()
        for val in numberlist:
            if val not in notprimelist:
                primes.append(val)
        return primes


def largestPrimeFactor(primeList):

    return primeList




