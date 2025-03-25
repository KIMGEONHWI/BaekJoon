import sys

N = int(sys.stdin.readline())

data = []

for _ in range(N):
    data.append(sys.stdin.readline().split())

for i in sorted(data, key=lambda x: int(x[0])):
    print(' '.join(i))