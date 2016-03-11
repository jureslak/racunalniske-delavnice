f = open("krog.txt", 'w')
n = 50
center = n/2
for i in range(n):
    for j in range(n):
        if (i - center)**2 + (j - center)**2 <= center**2:
            f.write('#')
        else:
            f.write('.')
    f.write('\n')
f.close()


f = open("slika.ppm", 'w')
f.write("P3\n")
f.write("# asdf\n")
n = 255
f.write("{} {}\n".format(n, n))
f.write("255\n")
for i in range(n):
    for j in range(n):
        r = i
        g = j
        b = 0
        f.write('{} {} {} '.format(r, g, b))
    f.write('\n')
f.close()

