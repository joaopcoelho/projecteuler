# projecteuler problem 99

from numpy import log



# read list of (base, exp)

with open("p099_base_exp.txt") as f:

    list_of_pairs = list(f)


list_of_pairs = [x.split(",") for x in list_of_pairs]
list_of_pairs = [(i+1, int(k), int(l)) for i,(k,l) in enumerate(list_of_pairs)]


# filter pairs that are obviously smaller
list_of_filtered_pairs = []
for pair in list_of_pairs:
    for pair0 in list_of_pairs:
        if pair[1] < pair0[1] and pair[2] < pair0[2]:
            break
        if pair[1] == pair0[1] and pair[2] < pair0[2]:
            break
        if pair[1] < pair0[1] and pair[2] < pair0[2]:
            break
    else:
        list_of_filtered_pairs.append(pair)


# log is strictly crescent so a>b => log(a) > log(b)
# also log(a**b) = b log(a)

list_of_log_pairs = [(i,e*log(b)) for (i,b,e) in list_of_filtered_pairs]

print sorted(list_of_log_pairs, key=lambda (i,x): -x)[0]


