w = int(input("Enter w: "))
t = int(input("Enter t: "))
a = []; b = []; c = []; e = 0

for i in range(0, t):
    a.append(int(input("Enter A" + str(i) + ": ")))
    b.append(int(input("Enter B" + str(i) + ": ")))
    if a[i]-b[i] < 0:
        c.append(int((a[i] - b[i]) + 2 ** w) - e)
    else:
        c.append(int(a[i] - b[i]) - e)
    if  0 <= a[i] - b[i] < (2 ** w):
        e = 0
    else:
        e = 1
c.reverse()
print(c)