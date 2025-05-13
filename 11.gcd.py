# Greatest common divisor
# Input: a, b
# Output: gcd(a, b)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
A = a; B = b

while B > 0:
    R = A % B
    A = B
    B = R

print(A)