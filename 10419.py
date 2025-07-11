T = int(input())
for _ in range(T):
    d = int(input())
    t = 0

    while (t + t * t) <= d:
        t += 1
    print(t - 1)
