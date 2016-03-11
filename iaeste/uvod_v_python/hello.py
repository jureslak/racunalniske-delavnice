print("hello world")
a = 5
b = "Janez"
c = [1, 5, 6, b]
d = 4.5
e = False
f = a + d
print(f)
f = f + f
b = d**f
print(f)
print(c, e)
print(b)
# print(c+f)
a = [a, d, f]
print(a)
a = a + c
print(a)
a.append(1243)
print(a)
a.pop()
print(a)
print(a[2])  # tretji element a
a[2] = "etka"
print(a)
print(len(a))
a.append(a[6] + ' M' + a[2])
print(a)

a = 5
b = "6"
c = a + int(b)
print(c)
a = str(a)
d = a + b
d = int(d)
print(d+2)

a = 5
b = "6"
print(int(str(a)+b)+2)

a = int(input("Vpisi stevilo: "))
b = int(input("Vpisi drugo stevilo: "))
print("Kvocient", a, "in", b, "je:", a/b)
print("Kvocient {} in {} je: {}".format(a, b, a/b))
