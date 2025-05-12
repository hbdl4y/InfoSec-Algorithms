import math

w = int(input("Enter W: "))
p = int(input("Enter p: "))
x = int(input("Enter x: "))
m = math.ceil(math.log(p, 2))
t = math.ceil(m / w) 
a = []

for i in reversed(range(0, t)):
    a.append(int(x / (2 ** (i * w))))
    x = x % (2 ** (i * w))
    print(a)
    print(x)
print(a)