import sys, math

A, B = map(int, sys.stdin.readline().split())

print(math.gcd(A, B))
print(math.lcm(A, B))