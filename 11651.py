import sys

N = int(sys.stdin.readline())

data = []

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    data.append([A, B])

data.sort(key=lambda x: (x[1], x[0])) #y좌표 기준으로 정렬, y좌표가 같은 경우에는 x좌표 기준으로 정렬


for num in data:
    print(num[0], num[1])