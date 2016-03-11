a = int(input())
if a % 2 == 0:
    print("Stevilo {} je sodo".format(a))
elif a > 8:
    print("Stevilo {} je vecje od 8".format(a))
else:
    print("Stevilo je brezveze")
    
print("konec")

b = a
while a > 0:
    print(a)
    a = a - 1
#    a -= 1

for i in range(b, -1, -1):
    print(i)

c = [1, 3, 4]
for i in range(len(c)):
    print(c[i])

for i in c:
    print(i)
