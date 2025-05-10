w = int(input("Enter W: "))
t = int(input("Enter t: "))
a = []; b = []; c = []; e = 0

for i in range(0, t):
    a.append(int(input("Enter A" + str(i) + ": ")))
    b.append(int(input("Enter B" + str(i) + ": ")))
    c.append(int((a[i] + b[i]) % (2 ** w)) + e)
    if  0 <= a[i] + b[i] < (2 ** w):
        e = 0
    else:
        e = 1
c.reverse()
print(c)