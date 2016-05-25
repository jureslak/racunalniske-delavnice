memo = {}
def ssum(n, i=0):
    if n <= 9: return i
    if (n, i) in memo: return memo[n, i]
    j = ssum(sum(map(int, str(n))), i+1)
    memo[n, i] = j
    return j

a = []
for i in range(100):
    a.append(ssum(i))
print(max(a))
