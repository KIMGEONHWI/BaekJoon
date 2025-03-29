## 첫번째 풀이 - 시간 초과

import sys
import math
from functools import reduce


N = int(sys.stdin.readline())

data = []

for _ in range(N):
    data.append(int(sys.stdin.readline().strip()))

current_gap = []

for i in range (len(data)-1):
    current_gap.append(data[i+1] - data[i])

max_gcd = reduce(math.gcd, current_gap)

first = data[0]
current_value = data[0]
garosu = [first]


while garosu[-1] <= data[-1]:

    if len(garosu) == 0:
        garosu.append(first)
    else:
        garosu.append(current_value + max_gcd)
        current_value += max_gcd

y = [x for x in garosu if x not in data]



print(len(y)-1)

##두번째 풀이 - 메모리 초과
import sys
import math
from functools import reduce

N = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(N)]

current_gap = [data[i+1] - data[i] for i in range(len(data) - 1)]
max_gcd = reduce(math.gcd, current_gap)

first = data[0]
current_value = data[0]
garosu = []

while current_value <= data[-1]:
    garosu.append(current_value)
    current_value += max_gcd

data_set = set(data)
y = [x for x in garosu if x not in data_set]

print(len(y))

##세번째 시도 - 성공!
import sys
import math

input = sys.stdin.readline

N = int(input())
positions = [int(input()) for _ in range(N)]

gaps = [positions[i+1] - positions[i] for i in range(N - 1)]

gcd_value = gaps[0]
for g in gaps[1:]:
    gcd_value = math.gcd(gcd_value, g)


total_add = sum((gap // gcd_value - 1) for gap in gaps)
print(total_add)

