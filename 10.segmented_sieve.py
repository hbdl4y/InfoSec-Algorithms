# Segmented sieve
# Input: n, d (Sieving block size)
# Output: All prime numbers smaller or equal to n

import math

def odd(a):
    for x in a:
        if x % 2 == 0:
            a.remove(x)
    return a # Removes all even numbers from a_block

def normal_sieve(a, n):
    c = []

    for p in a:
        for i in range (2, int(n / p) + 1):
            c.append(i * p)
        for x in c:
            if x in a:
                a.remove(x)
        c.clear()
    return a # Normal sieve. Used to find p (prime numbers smaller than sqrt(n))

def segmented_sieve(a, p, n, d):
    b = []; p.remove(2) # Removes 2 from p (Why is this important?) (The only even prime number is 2, DUH!)
    
    for i in range(int(n / (d * 2))):
        q = []; t = [True] * d # Boolean list with d values. False = Composite number. True = Prime number.
        a_block = a[i * d * 2: (i + 1) * d * 2] # Blocks with length of d.
        
        for j in range(len(p)):
            q.append(int(((-1 / 2) * (a_block[0] + 1 + p[j])) % p[j])) # Q: offset value for each P from start of block to first number divisible by P
                                                                       # The block is now only odd numbers, so: 101, 103, 105, etc. 
        odd(a_block)                                                   # But a_block[0] is pre-odd(), so: 100, very strange...
        for j in range(len(p)):
            while q[j] < d:
                t[q[j]] = False
                q[j] += p[j] # Determines the value (True or False) of each value on t

        for j in range(d):
            if t[j] == False:
                a_block[j] = 0
        while 0 in a_block:
            a_block.remove(0) # Maps t to a_block (There's probably a better way to do this!)
        b += a_block
    
    b.remove(1)
    print([2] + p + b) # Removing 1 and adding back 2 and p (But what if L != 0?)

n = int(input("Enter n: "))
d = int(input("Enter d: "))
a = [i for i in range(0, n + 1)]; p = [i for i in range(2, int(math.sqrt(n)))]
if d > math.sqrt(n):
    print("d has to be smaller than sqrt(n)! Try again!")
    exit()

normal_sieve(p, int(math.sqrt(n)) + 1)
segmented_sieve(a, p, n, d)