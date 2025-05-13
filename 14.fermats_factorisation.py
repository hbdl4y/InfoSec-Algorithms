# Fermat's factorisation method (to see if n is a prime number)
# Input: n, t
# Output: Whether n is a prime or a composite numbern according to the method

import random

def binary_exp(a, k, n):
    b = 1; A = a; k_list = []
    if k == 0:
        return b
    
    while (k > 0):
        k_list.append(k % 2)
        k = k // 2
    if k_list[0] == 1:
        b = a
    
    for i in range(1, len(k_list)):
        A = (A ** 2) % n
        if k_list[i] == 1:
            b = (A * b) % n
    return b

def fermat(n, t):
    for i in range(t):
        a = random.choice(range(2, n - 1))
        r = binary_exp(a, n - 1, n)
        if r != 1:
            return "Composite number."
    return "Prime number."

n = int(input("Enter n: "))
t = int(input("Enter t: "))

print(fermat(n , t))