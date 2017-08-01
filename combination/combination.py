#! /usr/bin/env python3

def combination(n,r):
    if r < 0 or r>n:
        return 0
    elif  r ==1 :
        return n
    elif r == n :
        return 1

    if r > n-r:
        r = n -r
    if r == 0 or  n<= 1 : 
        return 1
    return combination(n-1,r) + combination(n-1,r-1)

print (combination(990,33))

