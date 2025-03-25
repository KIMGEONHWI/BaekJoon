import sys

data = []

for i in range(5):
    data.append(int(sys.stdin.readline()))

average = sum(data) // 5

data.sort()
middle = data[2]

print(average)
print(middle)