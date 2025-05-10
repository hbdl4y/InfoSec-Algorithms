w = int(input("Enter W: "))
t = int(input("Enter t: "))
a = []; b = []; c = [0] * t*2

for i in range(0, t):
    a.append(int(input("Enter A" + str(i) + ": ")))
    b.append(int(input("Enter B" + str(i) + ": "))) 

for i in range (0, t):
    u = 0
    for j in range (0, t):
        uv = c[i + j] + (a[i] * b[j]) + u
        u = int(uv / (2 ** w))
        v = uv % (2 ** w)
        c[i + j] = v
    c[i + t] = u
c.reverse()
print(c)