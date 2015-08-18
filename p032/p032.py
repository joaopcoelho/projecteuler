# projecteuler problem 32
# pandigital products


def uniquedigits(max_N):
    """
    find the numbers with only unique digits 1-9 below max_N

    Input:
        max_N (integer)

    Returs:
        list of numbers with unique digits below max_N
    """

    lst = []
    for num in range(max_N+1):
        
        strnum = str(num)

        if "0" in strnum:
            continue

        c=0
        for i in "123456789":
            c = strnum.count(i)
            if c>1:
                break
        
        if c<2:
            lst.append(num)

    return lst

def numdigits(num):
    """
    find the number of digits in num
    """

    s = str(num)
    return len(s)

def pandigital(string):
    """
    checks whether a string is 1-9 pandigital
    """
    for i in "123456789":
            c = string.count(i)
            if c != 1:
                return False
    return True

unique4 = uniquedigits(10000)

list_of_products = []

for a in unique4:
    idxa = unique4.index(a)
    for b in unique4[idxa:]: # don't repeat x*Y and Y*x
        
        print a,b
        
        if numdigits(a) + numdigits(b) > 5:
            break # product will have at least 5 digits, so 10 digits total (max is 9)

        c = a*b

        if numdigits(a) + numdigits(b) + numdigits(c) != 9:
            continue # need 9 digits total

        abc = str(a)+str(b)+str(c)

        if pandigital(abc):
            list_of_products.append(c)


print sum(set(list_of_products)) # remove duplicates before sum