# projecteuler problem 13
# sum of large digits

f = open("p013_input.txt", "r")
numbers = list(f)
f.close()

numbers = [int(x) for x in numbers]
print sum(numbers)
