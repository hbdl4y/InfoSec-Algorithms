n = int(input("Enter n: "))
a = []; comp_num = []

for i in range(2, n + 1):
    a.append(i)

for p in a:
    for i in range(2, int(n / p) + 1):
        comp_num.append(i * p)
    for x in comp_num:
        if x in a:
            a.remove(x)
    comp_num.clear()
print(a)