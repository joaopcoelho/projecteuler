# projecteuler p004
# largest palindrome product


def ispalindrome(num):
    """
    checks whether a number is a palindrome
    palindrome: reads the same both ways"
    """

    s = str(num)

    if s == s[::-1]:
        return True
    else:
        return False

def test_ispalindrome():
    assert ispalindrome(29843) is False
    assert ispalindrome(123454321) is True

def largestpalindrome(num1, num2):
    """
    finds the largest palindrome as a product of n1*n2 where n1<num1 and n2<num2
    """

    imax=num1
    imin=1

    jmax=num2
    jmin=1

    pals = []

    for i in xrange(imax,imin,-1):
        for j in xrange(jmax,jmin,-1):
            p = i*j
            if ispalindrome(p):
                pals.append(p)
                imin=jmin

    return max(pals)

print largestpalindrome(999,999)

test_ispalindrome()