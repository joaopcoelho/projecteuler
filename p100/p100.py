# projecteuler P100
# arranged probability

import numpy as np


baseT = int(1e7)

lst = []

for T in xrange(1,baseT):
    x = (2 + np.sqrt( 4-8*T*(1-T)))/4.0

    if x.is_integer():
        lst.append((x,T))


xx = [x for (x,T) in lst]
tt = [t for (x,t) in lst]


dif = [tt[k]-xx[k] for k in range(len(xx))]
form = [(dif[k]-dif[k-2])*dif[k-1] for k in range(1,len(dif))]

# by printing dif and form a pattern starts to emerge: the values in form match the values in dif (which correspond to the RED discs) on every second step
# so a reasonable assumption might be that by some magic the formula that we use to obtain the values in form actually gives values for RED discs for which the 1/2 probability is verified
# using that we run form up to a high enough value and then solve for x=BLUE discs


likelyR = form[-1]


likelyX  = .5*((2*likelyR+1) + np.sqrt((2*likelyR+1)**2 + 4*likelyR*(likelyR-1)))

likelyX2 = .5*((2*likelyR+1) - np.sqrt((2*likelyR+1)**2 + 4*likelyR*(likelyR-1)))

print "{0:.5f}".format(likelyX2)
print "{0:.5f}".format(likelyX)

