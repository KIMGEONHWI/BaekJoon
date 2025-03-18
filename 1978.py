N = int(input())
data = list(map(int, input().split()))
answer = 0

for num in data:
    count = 0 
    for j in range(1, num+1):
        if num % j == 0:
            count += 1
    if count == 2:
        answer += 1

print(answer)