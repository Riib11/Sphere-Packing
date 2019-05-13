import itertools as it
import random
random.seed()

valid_codewords = [
    (0,0,0,0),
    (0,1,1,1),
    (1,0,0,1),
    (1,1,1,0)
]

valid_messages = [
    (0,0),
    (0,1),
    (1,0),
    (1,1)
]

def encode(a):
    i = (a[0] + a[1]) % 4
    return valid_codewords[i]

def inverse_encode(x):
    i = valid_codewords.index(x)
    return valid_messages[i]

p = 0.1
q = 1 - p

def noise(b):
    return (b + (0 if random.random() < q else 1)) % 2

def transmit(x):
    return tuple([ noise(xi) for xi in x ])

def distance(x, y):
    return len([ i for i in range(len(x)) if x[i] != y[i] ])

def decode(r):
    # decoded codeword
    y = None
    if r in valid_codewords:
        y = r
    else:
        for c in valid_codewords:
            if r[3] == c[3] and distance(r, c) == 1:
                y = c
    return inverse_encode(y)

F2 = (0,1)
for i in it.product(F2, repeat=4):
    
    print(i)


# results = [0,0]
# iterations = 100000
# for i in range(iterations):
#     heads = 0
#     tails = 1
#     a = (heads, tails) # in F_2
#     x = encode(a)      # in F_3
#     r = transmit(x)
#     b = decode(r)
#     # print(a,x,r,y)
#     # print('%s -encode-> %s -transmit-> %s -decode-> %s' % (a,x,r,b))
#     success = int(a == b)
#     results[success] += 1
#
# print("successes: %d" % results[1])
# print("failures:  %d" % results[0])
# print("success ratio: %f" % (results[1]/(results[0]+results[1])))
