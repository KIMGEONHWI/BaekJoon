import sys, math

N = int(sys.stdin.readline())

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(math.lcm(A, B))