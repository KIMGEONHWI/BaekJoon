import sys, math

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

numerator = a * d + b * c
denominator = b * d

g = math.gcd(numerator, denominator)

print(numerator // g, denominator // g)