import random

a = [0,0,0,0,0,0,0,0,0,0,]

for i in range(100000):
    n = random.randint(1, 10)
    a[n-1] = a[n-1] + 1


jaz = 100
igralnica = 100
c = 0
max_zasluzek = 0
while jaz > 0:
    n = random.randint(0, 1)
    if n == 0:
        jaz -= 1
        igralnica += 1
    else:
        jaz += 1
        igralnica -= 1
    if igralnica < 0:
        print("Wow")
        break
    
    if jaz - 100 > max_zasluzek:
        max_zasluzek = jaz - 100
        
    c += 1
print("Najvecji zasluzek: ", max_zasluzek)
print("Igrali smo: {} iger".format(c))
