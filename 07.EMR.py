a = int(input("Enter a: "))
b = int(input("Enter b: "))
if b > a:
    t = a; a = b; b = t

if b == 0:
    d = a; x = 1; y = 0
    print(str(d), str(x), str(y))
    exit()
x1 = 0; y1 = 1; x2 = 1; y2 = 0
while b > 0:
    q = int(a / b); r = a - (q * b); x = x2 - (q * x1); y = y2 - (q * y1)
    a = b; b = r; x2 = x1; x1 = x; y2 = y1; y1 = y
d = a; x = x2; y = y2
print(str(d), str(x), str(y))