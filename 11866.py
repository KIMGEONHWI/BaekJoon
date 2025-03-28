import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

people = deque()

for i in range(1, N+1):
    people.append(i)

result = []

while people:
    people.rotate(-(K - 1))
    result.append(people.popleft())
print(f"<{', '.join(map(str, result))}>")