def je_popolno(a):
    vsota = 0
    for i in range(1, a):  # za vsa stevila od 1 do a
        if a % i == 0:  # preverimo ali i deli a
           # print(i)
            vsota = vsota + i # ce ga, ga dodamo k vsoti

    if vsota == a:
        return True
    else:
        return False

a = int(input("Vnesi stevilo: "))


##vsota = 1
##i = 2
##while i*i < a:
##    if a % i == 0:  # preverimo ali i deli a
##        vsota = vsota + i # ce ga, ga dodamo k vsoti
##        vsota = vsota + int(a/i)
##    i += 1
##if i * i == a:
##    vsota += i


if je_popolno(a):
    print("{} je popolno".format(a))
else:
    print("{} ni popolno".format(a))


a = int(input("Vnesi stevilo: "))
for i in range(1, a+1):
    if je_popolno(i):
        print(i)
