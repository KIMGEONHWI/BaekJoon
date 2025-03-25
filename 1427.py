import sys

N = str(sys.stdin.readline())

data = []
li = ''

for i in N:
    data.append(i)

data.sort(reverse=True)

for j in data:
    li += j

print(li)
