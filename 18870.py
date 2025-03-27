import sys

N= int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))

data_set = sorted(dict.fromkeys(data))

dic = {}
for i in range(len(data_set)):
  dic[data_set[i]] = i

for i in data:
  print(dic[i], end=" ")