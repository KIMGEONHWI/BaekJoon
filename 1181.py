import sys

N = int(sys.stdin.readline())

data = []

for i in range(N):
    data.append(sys.stdin.readline().strip())

data.sort(key = lambda x: (len(x), x))
result = dict.fromkeys(data)

for i in result:
    print(i)