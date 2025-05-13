# Pollard's rho algorithm
# Input: n, t
# Output: A non-trivial factor of n or none.

def gcd(a, b):
    A = a; B = b
    while B > 0:
        R = A % B
        A = B
        B = R
    return A

def g(x, n):
    y = ((x ** 2) + 1) % n
    return y

n = int(input("Enter n: "))
t = int(input("Enter t: "))
a = 2; b = 2

for i in range(t):
    a = g(a, n)
    b = g(g(b, n), n)
    d = gcd(a - b, n)

    if 1 < d < n:
        res = [d, int(n / d)]
        print(res)
        exit()

print("No non-trivial factors found.")