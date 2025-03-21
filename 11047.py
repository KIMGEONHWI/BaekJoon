N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)


answer = 0
for coin in coins:
    if K >= coin:
        answer += K // coin
        K = K % coin    
print(answer)