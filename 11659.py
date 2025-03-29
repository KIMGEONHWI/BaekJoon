# 첫번째 시도 - 시간 초과
import sys

N, M = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

for _ in range(M):
    start, end = list(map(int, sys.stdin.readline().split()))
    range_sum = 0
    for i in range(start-1, end):
        range_sum += data[i]
    print(range_sum)


#두번째 시도 - 누적합 알고리즘 활용
import sys

N, M = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] * (N + 1)

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + data[i - 1]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(prefix_sum[end] - prefix_sum[start - 1])