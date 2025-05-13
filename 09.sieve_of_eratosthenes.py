# Sieve of Eratosthenes
# Input: n
# Output: All prime numbers smaller or equal to n

n = int(input("Enter n: "))
a = [i for i in range(2, n + 1)]; c = []

for p in a:
    for i in range(2, int(n / p) + 1):
        c.append(i * p)
    for x in c:
        if x in a:
            a.remove(x)
    c.clear()

print(a)