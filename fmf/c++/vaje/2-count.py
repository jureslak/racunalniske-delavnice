from collections import Counter
with open("anailza1.txt") as f:
    c = Counter(f.read().split())

for p in c.most_common(50):
    print(*p[::-1])
