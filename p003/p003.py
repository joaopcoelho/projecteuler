# projecteuler problem 3
# largest prime factor

def getprimes(max_N):
    """
    get list of prime numbers up to max_N

    Input:
        max_N: integer
    
    Returns:
        primes: set of prime numbers
    """
    assert max_N > 2
    assert type(max_N) is int 

    primes = [2]

    for num in xrange(2,max_N+1):
        primedivs = [num%p for p in primes]
        minimum = min(primedivs)

        if minimum == 0:
            pass # is not prime
        else:
            primes.append(num)

    return set(primes)



def primefactors(N):
    """
    returns the prime factors of N

    Input:
        N (integer)
    Returns:
        factors (list): set of prime factors of N
    """    

    primes = getprimes(10000) # arbitrary number, happens to work
    factors = []

    product=1
    num = N

    for p in primes:
        if num%p == 0:
            factors.append(p)
            product = product*p
            num=num/p
        
        try:
            if reduce(lambda x,y: x*y, factors) == N:
                return factors
        except TypeError:
            pass


def test_primefactors():
    try:
        assert primefactors(13195) == [5,7,13,29]
    except:
        print primefactors(13195)
        raise AssertionError


res = primefactors(600851475143)

print res


test_primefactors()