def sestej(s):
    vsota = s[0]
    for i in range(1, len(s)):
        vsota += s[i]
    return vsota


s = [1,2,3,4,5,3]
print(sestej(s))

s = ["gsadf", "qwe", "kjw"]
print(sestej(s))
