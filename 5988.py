N = int(input())
for _ in range(N):
    K = input().strip()
    if int(K[-1]) % 2 == 0:
        print('even')
    else:
        print('odd')
