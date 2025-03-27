import sys

N = int(sys.stdin.readline())

data = []
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    data.append([A, B])

data.sort()

for num in range(N):
    print(data[num][0], data[num][1])