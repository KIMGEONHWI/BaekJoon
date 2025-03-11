N, M = map(int, input().split())

baskets = []

for x in range(1, N+1):
    baskets.append(x)
for _ in range(M):
    i, j = map(int, input().split())
    baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]

print(" ".join(map(str, baskets)))
