import sys

N = int(sys.stdin.readline())

stack = []

data = []

for i in range(N):
    data.append(int(sys.stdin.readline()))

for num in data:
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))