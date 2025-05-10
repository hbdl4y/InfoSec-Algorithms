p = int(input("Enter p: "))
a = int(input("Enter a: ")) % p

u = a; v = p; x1 = 1; x2 = 0
if u == 0:
    print("Doesn't exist.")
    exit()
while u != 1:
    q = int(v / u); r = v - (q * u); x = x2 - (q * x1)
    v = u; u = r; x2 = x1; x1 = x
print(x1)