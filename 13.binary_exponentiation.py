# Binary exponentiation (to compute x ** k (mod n))
# Input: a ** k (mod n)
# Output: b (mod n), b in [0, n], a ** k = b (mod n)

a = int(input("Enter a: "))
k = int(input("Enter k: "))
n = int(input("Enter n: "))
b = 1; A = a; k_list = []

if k == 0:
    print(b)
    exit()

while (k > 0):
    k_list.append(k % 2)
    k = k // 2 # Converting k into binary
if k_list[0] == 1:
    b = a # An additional a for odd numbers

for i in range(1, len(k_list)):
    A = (A ** 2) % n 
    if k_list[i] == 1:
        b = (A * b) % n

print(b)

