# projecteuler problem 2
# even Fibonacci numbers

def nextfib(n1,n2):
    """
    generate the next number in the Fibonacci sequence

    Input:
        n1: integer (term n-2)
        n2: integer (term n-1)
    
    Returns:
        n: integer
    """
    n=n1+n2
    return n

def fibsequence(N):
    """
    return the Fibonacci sequence whose elements do not exceed N

    Input:
        N: maximum Fibonacci number (integer)

    Returns:
        fiblist: list of Fibonacci numbers
    """

    n=0
    n1=1
    n2=1
    fiblist = [n1,n2]

    while n<N:
        n = nextfib(n1,n2)
        if n<N:
            fiblist.append(n)

        n1=n2
        n2=n

    return fiblist

def sum_even_fibs(maxN):
    """
    sums even terms in fibonacci sequence where max value is maxN

    Input:
        maxN (integer)

    Returns:
        s: sum of fibonacci elements (integer)
    """

    # in fibonacci sequence, only every third number is even (because sum of two odds)

    fibs = fibsequence(maxN)
    fibs_even = fibs[2::3]
    s = sum(fibs_even)


    return s

def test_fibsequence():
    t1 = fibsequence(1000)
    try:
        assert t1 == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
    except AssertionError:
        print t1
        raise AssertionError

def test_sum_even_fibs():
    t1 = sum_even_fibs(10)
    try:
        assert t1 == 10
    except AssertionError:
        print t1
        raise AssertionError


maxfib = 4000000

print sum_even_fibs(maxfib)

test_fibsequence()
test_sum_even_fibs()