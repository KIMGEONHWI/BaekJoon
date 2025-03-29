import sys

N, M = map(int, sys.stdin.readline().split())


N_set = set()

for _ in range(N):
    data = sys.stdin.readline().strip()
    N_set.add(data)

count = 0
for _ in range(M):
    data = sys.stdin.readline().strip()
    if data in N_set:
        count += 1
print(count)