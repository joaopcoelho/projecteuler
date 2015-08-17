# project euler p014
# longest Collatz sequence



import operator

def next_collatz_term(n):
    """
    implements rules for next term in collatz sequence

    Input: 
        n: integer

    Output:
        result of applying collatz rules (integer)
    """

    assert (type(n) is int)
    if n%2 == 0:
        return n/2
    else:
        return 3*n +1


def pow2(n):
    """
    lists powers of two smaller than or equal to n

    Input:
        n: integer

    Output:
        lst: a list of numbers (powers of two smaller or equal to n) in DESCENDING ORDER
    """

    k=1
    iterator=1
    pows = []

    while k<=n:
        pows.append(k) 
        k = 2**iterator
        iterator+=1
        

    return pows[::-1]


def collatz_sequence(n):
    """
    DEPRECATED: use improved_collatz_sequence
    calculates the collatz sequence of a number n

    Input:
        n: integer

    Output:
        collatz_seq: a list of numbers forming the collatz sequence for n
    """
    assert (type(n) is int)

    powersoftwo = pow2(n)

    collatz_seq = [n]
    while n>1:

        if n in powersoftwo:

            idx = powersoftwo.index(n)
            collatz_seq.extend(powersoftwo[idx+1:])
            return collatz_seq  

        n = next_collatz_term(n)
        collatz_seq.append(n)


    return collatz_seq

def improved_collatz_sequence(n, dic):
    """
    calculates the lenght of the collatz sequence of a number n
    receives a dictionary with (starting_number: lenght_of_collatz_sequence) to avoid recomputing known sequences

    Input:
        n: integer
        dic: dictionary of (starting_number, lenght_of_collatz_sequence)

    Output:
        collatz_len: the lenght of the collatz sequence for number n
    """
    assert (type(n) is int)
    assert type(dic) is dict


    collatz_len=1
    while n>1:

        if n in dic:

            collatz_len += dic[n]-1
            return collatz_len
        else:
            n = next_collatz_term(n)
            collatz_len+=1


    return collatz_len




def test_collatz_sequence():
    start = 13
    colseq = collatz_sequence(start)

    assert len(colseq) == 10
    assert colseq == [13,40,20,10,5,16,8,4,2,1]



def test_pow2():

    assert len(pow2(4)) == 3
    assert len(pow2(1000)) == 10
    assert pow2(1024) == [1,2,4,8,16,32,64,128,256,512,1024][::-1]


def test_improved_collatz_sequence():
    test1 = improved_collatz_sequence(13, {1:1, 2:2, 8:4})
    assert test1 == 10



# which starting number below 1M produces the longest sequence?

collatzlens = {1:1}
max_starting_number = 1000000

for starting_number in xrange(max_starting_number):
    collatzlens[ starting_number] = improved_collatz_sequence(starting_number, collatzlens)


print sorted(collatzlens.items(), key=operator.itemgetter(1))[-1]



# run tests

test_pow2()
test_collatz_sequence()
test_improved_collatz_sequence()

