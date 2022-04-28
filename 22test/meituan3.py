mystr = input().split(" ")
n, m = int(mystr[0]), int(mystr[1])

mystr = input().split(" ")
L = []
for item in mystr:
    L.append(int(item))

mystr = input().split(" ")
R = []
for item in mystr:
    R.append(int(item))

N = [0 for _ in range(n)]

for i in range(m):
    for j in range(L[i]-1, R[i]):
        N[j] += 1

ans = 0
for i in N:
    if i > 1:
        ans += 1

print(ans)