y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

if m2 > m1 or (m2 == m1 and d2 >= d1):
    print(y2-y1)
else:
    print(y2-y1-1)

print(y2-y1+1)

print(y2-y1)