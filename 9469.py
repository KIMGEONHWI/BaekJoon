P = int(input())
for _ in range(P):

    N, D, A, B, F = input().split()
    N = int(N)
    D = float(D)
    A = float(A)
    B = float(B)
    F = float(F)

    t = D / (A + B)

    distance = F * t
    print(f"{N} {distance:.6f}")