def list_input(a, list_name, t):
    for i in range(0, t):
        a.append(int(input("Enter " + list_name + str(i) + ": ")))
    return a

def bdddm(x, a, w, t):
    for i in reversed(range(0, t)):
        a.append(int(x / (2 ** (i * w))))
        x = x % (2 ** (i * w))
    return a

def ccxb(a, b, c, w, t, e):
    for i in range(0, t):
        c.append(int((a[i] + b[i]) % (2 ** w)) + e)
        if  0 < a[i] + b[i] < (2 ** w):
            e = 0
        else:
            e = 1
    return c, e

def tcxb(a, b, c, w, t, e):
    for i in range(0, t):
        if a[i] - b[i] < 0:
            c.append(int((a[i] - b[i]) + 2 ** w) - e)
        else:
            c.append(int(a[i] - b[i]) - e)
        if  0 <= a[i] - b[i] < (2 ** w):
            e = 0
        else:
            e = 1
    return c, e

p = int(input("Enter p: "))
w = int(input("Enter W: "))
t = int(input("Enter t: "))
a = []; b = []; c1 = []; p_list = []; c2 = []; e = 0

list_input(a, "A", t)
list_input(b, "B", t)
tcxb(a, b, c1, w, t, e)

if e == 1:
    bdddm(p, p_list, t, w)
    ccxb(c1, p_list, c2, w, t, 1)
    c2.reverse()
    print(c2)
else:
    c1.reverse()
    print(c1)