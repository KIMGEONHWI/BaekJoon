#계수 정렬 활용

import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 10001  # 숫자가 1~10000이니까, 인덱스를 그대로 쓰려고 10001개 만듦

for _ in range(N):
    num = int(input())
    count[num] += 1  # 해당 숫자가 몇 번 나왔는지 기록

# 정렬된 순서대로 출력
for i in range(1, 10001):
    if count[i] > 0:
        for _ in range(count[i]):
            sys.stdout.write(f"{i}\n")  # 숫자 i를 count[i]번 출력