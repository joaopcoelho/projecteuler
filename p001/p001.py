# projecteuler problem 1
# multiples of 3 and 5

multiples = [x for x in range(1000) if x%3 == 0 or x%5 == 0]

print sum(multiples)