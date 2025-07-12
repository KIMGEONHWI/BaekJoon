T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    U = 2 * M - N
    T_ = N - M
    print(f"{U} {T_}")
